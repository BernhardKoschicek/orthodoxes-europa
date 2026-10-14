"""Tests for media serving, thumbnail generation and legacy fallback."""
from collections.abc import Generator
from pathlib import Path
import pytest
from flask.testing import FlaskClient
from PIL import Image

from app import app
from app.media import generate_thumbnail


@pytest.fixture
def temp_media(tmp_path: Path) -> Generator[Path, None, None]:
    """Prepare a temporary media directory with test images."""
    media_dir = tmp_path / "media"
    images_dir = media_dir / "images"
    repo_dir = media_dir / "repository"
    images_dir.mkdir(parents=True)
    repo_dir.mkdir(parents=True)

    # Create dummy jpeg
    test_img = images_dir / "sample.jpg"
    img = Image.new("RGB", (800, 600), color=(255, 0, 0))
    img.save(test_img, "JPEG")

    # Create dummy png
    test_png = images_dir / "sample.png"
    img_png = Image.new("RGBA", (400, 300), color=(0, 255, 0, 128))
    img_png.save(test_png, "PNG")

    # Create dummy palette image
    test_p = images_dir / "sample_p.jpg"
    img_p = Image.new("P", (100, 100))
    img_p.save(test_p, "PNG")

    # Create dummy cmyk image
    test_cmyk = images_dir / "sample_cmyk.jpg"
    img_cmyk = Image.new("CMYK", (100, 100))
    img_cmyk.save(test_cmyk, "JPEG")

    # Create dummy pdf
    dummy_pdf = repo_dir / "doc.pdf"
    dummy_pdf.write_bytes(b"%PDF-1.4 dummy content")

    orig_media = app.config["MEDIA_PATH"]
    app.config["MEDIA_PATH"] = media_dir
    yield media_dir
    app.config["MEDIA_PATH"] = orig_media


def test_generate_thumbnail_and_mtime_caching(temp_media: Path) -> None:
    """Verify thumbnail generation and incremental mtime checking."""
    src = temp_media / "images" / "sample.jpg"
    thumb = temp_media / "thumbnails" / "200x200" / "images" / "sample.jpg"

    res1 = generate_thumbnail(src, thumb, (200, 200))
    assert res1.exists()
    mtime1 = res1.stat().st_mtime

    # Second call should use cached thumbnail
    res2 = generate_thumbnail(src, thumb, (200, 200))
    assert res2 == res1
    assert res2.stat().st_mtime == mtime1


def test_generate_thumbnail_formats_and_modes(temp_media: Path) -> None:
    """Verify PNG, Palette and CMYK image mode thumbnail generation."""
    # PNG format
    src_png = temp_media / "images" / "sample.png"
    thumb_png = (
        temp_media / "thumbnails" / "100x100" / "images" / "sample.png")
    res_png = generate_thumbnail(src_png, thumb_png, (100, 100))
    assert res_png.exists()

    # Palette image to JPEG
    src_p = temp_media / "images" / "sample_p.jpg"
    thumb_p = (
        temp_media / "thumbnails" / "50x50" / "images" / "sample_p.jpg")
    res_p = generate_thumbnail(src_p, thumb_p, (50, 50))
    assert res_p.exists()

    # CMYK image
    src_cmyk = temp_media / "images" / "sample_cmyk.jpg"
    thumb_cmyk = (
        temp_media / "thumbnails" / "50x50" / "images" / "sample_cmyk.jpg")
    res_cmyk = generate_thumbnail(src_cmyk, thumb_cmyk, (50, 50))
    assert res_cmyk.exists()


@pytest.mark.usefixtures("temp_media")
def test_serve_media_success_and_errors(client: FlaskClient) -> None:
    """Test serving existing and non-existing media files."""
    response = client.get("/media/repository/doc.pdf")
    assert response.status_code == 200
    assert response.data.startswith(b"%PDF")

    # Non-existent
    response_404 = client.get("/media/images/missing.jpg")
    assert response_404.status_code == 404

    # Path traversal attempt
    response_traversal = client.get("/media/../../../etc/passwd")
    assert response_traversal.status_code in (404, 400)


@pytest.mark.usefixtures("temp_media")
def test_serve_thumbnail_on_demand_and_alt_source(
    client: FlaskClient) -> None:
    """Test on-demand thumbnail route and fallback to images/ subpath."""
    response = client.get("/media/thumbnails/100x100/images/sample.jpg")
    assert response.status_code == 200

    # Alt source lookup: requesting sample.png resolves to images/sample.png
    resp_alt = client.get("/media/thumbnails/100x100/sample.png")
    assert resp_alt.status_code == 200

    # Invalid dimensions
    resp_bad = client.get("/media/thumbnails/0x100/images/sample.jpg")
    assert resp_bad.status_code == 400

    # Missing image
    resp_missing = client.get("/media/thumbnails/100x100/images/absent.jpg")
    assert resp_missing.status_code == 404


@pytest.mark.usefixtures("temp_media")
def test_legacy_static_fallback(client: FlaskClient) -> None:
    """Test legacy static paths fallback to storage media."""
    # Legacy repository
    resp_repo = client.get("/static/repository/doc.pdf")
    assert resp_repo.status_code == 200

    # Missing legacy repository
    resp_missing = client.get("/static/repository/missing.pdf")
    assert resp_missing.status_code == 404

    # Legacy image
    resp_img = client.get("/static/images/sample.jpg")
    assert resp_img.status_code == 200

    # Missing legacy image
    resp_img_missing = client.get("/static/images/missing_img.jpg")
    assert resp_img_missing.status_code == 404

    # Thumbnail path traversal attempt
    resp_trav = client.get(
        "/media/thumbnails/100x100/../../../../etc/passwd")
    assert resp_trav.status_code in (400, 404)

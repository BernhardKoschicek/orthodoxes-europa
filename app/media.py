"""Media and thumbnail management using Pillow."""
from pathlib import Path
from flask import (
    Blueprint,
    Response,
    abort,
    current_app,
    send_from_directory)
from PIL import Image, ImageOps

media_bp: Blueprint = Blueprint("media", __name__)


def generate_thumbnail(
    source_path: Path,
    thumb_path: Path,
    size: tuple[int, int]) -> Path:
    """Generate a thumbnail incrementally checking modification time."""
    if thumb_path.exists():
        if thumb_path.stat().st_mtime >= source_path.stat().st_mtime:
            return thumb_path

    thumb_path.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source_path) as raw_img:
        img: Image.Image = ImageOps.exif_transpose(raw_img)
        is_jpeg = thumb_path.suffix.lower() in (".jpg", ".jpeg")
        if is_jpeg and img.mode in ("RGBA", "LA", "P"):
            background = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode == "P":
                img = img.convert("RGBA")
            background.paste(img, mask=img.split()[-1])
            img = background
        elif img.mode not in ("RGB", "RGBA", "L"):
            img = img.convert("RGB")

        img.thumbnail(size, Image.Resampling.LANCZOS)
        if is_jpeg:
            img.save(thumb_path, quality=85, optimize=True)
        else:
            img.save(thumb_path, optimize=True)

    return thumb_path


@media_bp.route("/media/<path:filename>")
def serve_media(filename: str) -> Response:
    """Serve persistent media files from the storage media directory."""
    media_dir = Path(current_app.config["MEDIA_PATH"]).resolve()
    target_path = (media_dir / filename).resolve()
    if not target_path.is_relative_to(media_dir) or not target_path.is_file():
        abort(404)
    return send_from_directory(
        target_path.parent,
        target_path.name)


@media_bp.route(
    "/media/thumbnails/<int:width>x<int:height>/<path:filename>")
def serve_thumbnail(
    width: int,
    height: int,
    filename: str) -> Response:
    """Serve cached thumbnail or generate on-demand if missing/stale."""
    if width <= 0 or height <= 0 or width > 3840 or height > 2160:
        abort(400)

    media_dir = Path(current_app.config["MEDIA_PATH"]).resolve()
    source_path = (media_dir / filename).resolve()
    if not source_path.is_relative_to(media_dir) or not source_path.is_file():
        # Fallback check under media_dir / 'images' / filename
        alt_source = (media_dir / "images" / filename).resolve()
        if alt_source.is_relative_to(media_dir) and alt_source.is_file():
            source_path = alt_source
            filename = f"images/{filename}"
        else:
            abort(404)

    thumb_rel = Path("thumbnails") / f"{width}x{height}" / filename
    thumb_path = (media_dir / thumb_rel).resolve()
    if not thumb_path.is_relative_to(media_dir):
        abort(400)

    generate_thumbnail(source_path, thumb_path, (width, height))
    return send_from_directory(
        thumb_path.parent,
        thumb_path.name)


@media_bp.route("/static/repository/<path:filename>")
def legacy_repository(filename: str) -> Response:
    """Legacy compatibility route for repository downloads."""
    media_dir = Path(current_app.config["MEDIA_PATH"]).resolve()
    target = (media_dir / "repository" / filename).resolve()
    if not target.is_relative_to(media_dir) or not target.is_file():
        abort(404)
    return send_from_directory(target.parent, target.name)

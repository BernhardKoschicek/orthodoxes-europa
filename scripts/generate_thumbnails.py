"""CLI script to incrementally generate media thumbnails."""
import argparse
from pathlib import Path
import sys

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from app.config import Config
from app.media import generate_thumbnail

DEFAULT_SIZES = [(200, 200), (400, 300), (800, 600)]
SUPPORTED_EXTS = {".jpg", ".jpeg", ".png", ".webp"}


def run_batch_thumbnails(media_dir: Path) -> tuple[int, int]:
    """Generate thumbnails for all images under media_dir."""
    images_dir = media_dir / "images"
    if not images_dir.is_dir():
        print(f"Directory {images_dir} does not exist.")
        return 0, 0

    generated = 0
    skipped = 0

    for path in images_dir.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in SUPPORTED_EXTS:
            continue
        rel_path = path.relative_to(media_dir)
        for width, height in DEFAULT_SIZES:
            thumb_path = (
                media_dir / "thumbnails" / f"{width}x{height}" / rel_path)
            if (
                thumb_path.exists()
                and thumb_path.stat().st_mtime >= path.stat().st_mtime):
                skipped += 1
                continue
            try:
                generate_thumbnail(path, thumb_path, (width, height))
                generated += 1
            except Exception as err:  # pylint: disable=broad-exception-caught
                print(f"Error generating thumbnail for {path}: {err}")

    return generated, skipped


def main() -> None:
    """CLI entrypoint."""
    parser = argparse.ArgumentParser(description="Pre-generate thumbnails")
    parser.add_argument(
        "--media-dir",
        type=Path,
        default=Config.MEDIA_PATH,
        help="Path to media directory")
    args = parser.parse_args()

    print(f"Processing thumbnails in {args.media_dir}...")
    gen, skip = run_batch_thumbnails(args.media_dir)
    print(f"Done: {gen} generated, {skip} up-to-date.")


if __name__ == "__main__":
    main()

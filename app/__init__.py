"""Application package initialization."""
from pathlib import Path
from flask import Flask, Response, request, send_from_directory

from app.config import Config


def _register_hooks(flask_app: Flask) -> None:
    """Register request hooks and security headers."""
    @flask_app.before_request
    def check_static_fallback() -> Response | None:
        """Fallback for media files requested via legacy static path."""
        path = request.path
        media_root = Path(flask_app.config["MEDIA_PATH"]).resolve()
        if path.startswith("/static/images/"):
            rel_name = path[len("/static/images/"):]
            static_dir = Path(flask_app.static_folder or "app/static")
            static_file = (static_dir / "images" / rel_name).resolve()
            if not static_file.exists():
                media_file = (media_root / "images" / rel_name).resolve()
                if (
                    media_file.is_relative_to(media_root)
                    and media_file.is_file()):
                    return send_from_directory(
                        media_file.parent,
                        media_file.name)
        elif path.startswith("/static/repository/"):
            rel_name = path[len("/static/repository/"):]
            media_file = (media_root / "repository" / rel_name).resolve()
            if (
                media_file.is_relative_to(media_root)
                and media_file.is_file()):
                return send_from_directory(
                    media_file.parent,
                    media_file.name)
        return None

    @flask_app.after_request
    def apply_caching(response: Response) -> Response:
        """Apply security headers to all responses."""
        response.headers[
            "Strict-Transport-Security"
        ] = "max-age=31536000; includeSubDomains"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "SAMEORIGIN"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        return response


app: Flask = Flask(__name__)
app.config.from_object(Config)

# pylint: disable=wrong-import-position
from app.media import media_bp
from app.util import filters
from app.view import init_views

app.register_blueprint(filters.blueprint)
app.register_blueprint(media_bp)
_register_hooks(app)
init_views(app)


def create_app(config_class: type[Config] = Config) -> Flask:
    """Application factory for testing or multi-instance setups."""
    if config_class == Config and app is not None:
        return app

    new_app = Flask(__name__)
    new_app.config.from_object(config_class)
    new_app.register_blueprint(filters.blueprint)
    new_app.register_blueprint(media_bp)
    _register_hooks(new_app)
    init_views(new_app)
    return new_app


if __name__ == "__main__":  # pragma: no cover
    app.run()

"""Route handlers and views for orthodoxes-europa."""
from flask import Flask, render_template

from app.data.index import front_menu, home_gallery
from app.data.projects import project_gallery, projects_
from app.data.public_relations import public
from app.data.publications import publications
from app.data.software import software
from app.data.team import team_


def init_views(app: Flask) -> None:
    """Register all application routes onto the Flask application."""

    @app.route("/health")
    def health() -> tuple[dict[str, str], int]:
        """Health check endpoint for container orchestrators."""
        return {"status": "ok", "version": str(app.config.get(
            "VERSION", "0.1.0"))}, 200

    @app.route("/")
    def home() -> str:
        """Render front landing page."""
        return render_template(
            "home.html",
            front_menu=front_menu,
            home_gallery=home_gallery)

    @app.errorhandler(404)
    def page_not_found(e: Exception) -> tuple[str, int]:
        """Render 404 error page."""
        return render_template("404.html", e=e), 404

    @app.route("/about")
    def about() -> str:
        """Render about page."""
        return render_template("about.html")

    # pylint: disable=non-ascii-name
    @app.route("/öffentlichkeitsarbeit")
    def öffentlichkeitsarbeit() -> str:
        """Render public relations page."""
        return render_template("public.html", public=public)

    # pylint: disable=non-ascii-name
    @app.route("/veröffentlichungen")
    def veröffentlichungen() -> str:
        """Render publications list page."""
        return render_template(
            "veroeffentlichungen.html",
            publications=publications)

    @app.route("/download")
    def download() -> str:
        """Render downloads page."""
        categories: list[str] = []
        for pub in publications.values():
            cat = pub.get("category")
            if isinstance(cat, list):
                categories.extend(str(c) for c in cat)
        return render_template(
            "download.html",
            publications=publications,
            software=software,
            category=categories)

    @app.route("/geoportal")
    def geoportal() -> str:
        """Render interactive geoportal embed."""
        return render_template("geoportal.html")

    @app.route("/impressum")
    def impressum() -> str:
        """Render legal notice page."""
        return render_template("impressum.html")

    @app.route("/team")
    def team() -> str:
        """Render team members page."""
        return render_template("team.html", team=team_)

    @app.route("/projekte", methods=["GET"])
    @app.route("/projekte/<projekt>", methods=["GET"])
    def projekte(projekt: str | None = None) -> str:
        """Render projects overview or specific project details."""
        if projekt:
            return render_template(
                "projekt_details/projekt_layout.html",
                projekt=projects_[projekt],
                gallerie=project_gallery)
        return render_template("projekte.html", projects=projects_)

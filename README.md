# Orthodoxes Europa

Digitales Geoportal der Geschichte der Orthodoxen in Österreich.

## Technical Stack

- **Backend:** Python 3 with [Flask](https://flask.palletsprojects.com/)
- **Frontend:** HTML5, CSS3, [Bootstrap 5](https://getbootstrap.com/), [jQuery](https://jquery.com/)
- **Data:** Structured Python dictionaries and lists (static data approach)

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the application

```bash
python runserver.py
```

The application will be available at `http://127.0.0.1:5000`.

## Project Structure

- `orthodoxes_europa/`: Main application package
  - `data/`: Data definitions for the site (projects, team, publications, etc.)
  - `static/`: Static assets (images, styles, geoportal)
  - `templates/`: Jinja2 templates for the UI
  - `util/`: Utility functions and Jinja2 filters
- `runserver.py`: Entry point for running the development server

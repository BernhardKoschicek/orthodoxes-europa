#!/usr/bin/env bash
# Automated deployment script for Orthodoxes Europa
set -euo pipefail

PORT="${PORT:-5000}"
HEALTH_URL="http://127.0.0.1:${PORT}/health"
FORCE="${1:-}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"

echo "=== Starte Deployment für Orthodoxes Europa ==="

# 1. Ermitteln des Tracking-Branches
git fetch origin

UPSTREAM_BRANCH="$(git rev-parse --abbrev-ref --symbolic-full-name @{u} 2>/dev/null || true)"
if [ -z "$UPSTREAM_BRANCH" ]; then
    if git rev-parse --verify origin/main &>/dev/null; then
        UPSTREAM_BRANCH="origin/main"
    elif git rev-parse --verify origin/master &>/dev/null; then
        UPSTREAM_BRANCH="origin/master"
    fi
fi

LOCAL_COMMIT="$(git rev-parse HEAD)"
REMOTE_COMMIT="$(git rev-parse "$UPSTREAM_BRANCH")"

if [ "$LOCAL_COMMIT" = "$REMOTE_COMMIT" ] && [ "$FORCE" != "--force" ]; then
    echo "Bereits auf dem neuesten Stand ($UPSTREAM_BRANCH: $LOCAL_COMMIT). Kein Update erforderlich."
    echo "Verwende '$0 --force' zum Erzwingen."
    exit 0
fi

echo "Aktualisiere von $LOCAL_COMMIT auf $REMOTE_COMMIT..."
git pull --ff-only

# 2. Container oder venv aktualisieren
if command -v podman &>/dev/null && [ -f "compose.yaml" ]; then
    echo "Aktualisiere Podman Container..."
    podman compose build
    podman compose up -d
else
    echo "Aktualisiere Python venv via uv..."
    uv sync
    if command -v systemctl &>/dev/null && systemctl is-active --quiet orthodoxes-europa; then
        sudo systemctl restart orthodoxes-europa
    fi
fi

# 3. Thumbnails inkrementell aktualisieren
if [ -f "scripts/generate_thumbnails.py" ]; then
    echo "Prüfe und aktualisiere Thumbnails inkrementell..."
    uv run python scripts/generate_thumbnails.py || true
fi

# 4. Validierung des /health-Endpunkts
echo "Validiere /health Endpunkt an $HEALTH_URL..."
MAX_RETRIES=15
DELAY=2
SUCCESS=false

for i in $(seq 1 $MAX_RETRIES); do
    STATUS_CODE=$(curl -s -o /tmp/health_response.json -w "%{http_code}" "$HEALTH_URL" || true)
    if [ "$STATUS_CODE" = "200" ]; then
        if grep -q '"status":\s*"ok"' /tmp/health_response.json 2>/dev/null; then
            echo "Health-Check erfolgreich! Server antwortet mit Status 200 und status: ok."
            cat /tmp/health_response.json
            echo ""
            SUCCESS=true
            break
        fi
    fi
    echo "Warte auf App-Bereitschaft (Versuch $i/$MAX_RETRIES - HTTP $STATUS_CODE)..."
    sleep $DELAY
done

if [ "$SUCCESS" = false ]; then
    echo "FEHLER: Health-Check nach $((MAX_RETRIES * DELAY)) Sekunden fehlgeschlagen!"
    exit 1
fi

echo "=== Deployment erfolgreich abgeschlossen! ==="

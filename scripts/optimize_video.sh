#!/usr/bin/env bash
# Optimize video for HTML5 playback with +faststart (moov atom at beginning)
set -euo pipefail

if [ "$#" -lt 2 ]; then
    echo "Verwendung: $0 <input_video> <output_video.mp4>"
    echo "Beispiel: $0 raw_recording.mov storage/media/videos/vortrag.mp4"
    exit 1
fi

INPUT="$1"
OUTPUT="$2"

if ! command -v ffmpeg &> /dev/null; then
    echo "Fehler: 'ffmpeg' ist nicht installiert. Bitte mit 'apt install ffmpeg' installieren."
    exit 1
fi

mkdir -p "$(dirname "$OUTPUT")"

echo "Optimiere Video: $INPUT -> $OUTPUT mit +faststart..."
ffmpeg -i "$INPUT" \
    -c:v libx264 \
    -preset medium \
    -crf 23 \
    -c:a aac \
    -b:a 128k \
    -movflags +faststart \
    -y "$OUTPUT"

echo "Erfolgreich optimiert: $OUTPUT"

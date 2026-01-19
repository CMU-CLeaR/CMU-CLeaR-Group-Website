#!/bin/bash
set -euo pipefail

echo "Entry point script running"

CONFIG_FILE=_config.yml

# Check if JEKYLL_DRAFTS environment variable is set to include drafts
DRAFTS_FLAG=""
if [ "${JEKYLL_DRAFTS:-false}" = "true" ]; then
    echo "Draft mode enabled - drafts will be visible"
    DRAFTS_FLAG="--drafts"
fi

start_jekyll() {
    bundle exec jekyll serve --watch --port=8080 --host=0.0.0.0 --livereload --verbose --trace --force_polling $DRAFTS_FLAG &
}

start_jekyll

while true; do
    inotifywait -q -e modify,move,create,delete $CONFIG_FILE
    if [ $? -eq 0 ]; then
        echo "Change detected to $CONFIG_FILE, restarting Jekyll"
        jekyll_pid=$(pgrep -f jekyll)
        kill -KILL $jekyll_pid
        start_jekyll
    fi
done

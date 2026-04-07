#!/bin/bash
# Pass through without modification when:
# 1. Running as Node.js (CLI mode) - ELECTRON_RUN_AS_NODE is set
# 2. Running as a child/renderer process - args contain --type=
if [[ -n "$ELECTRON_RUN_AS_NODE" ]] || [[ "$*" == *"--type="* ]]; then
    exec /usr/share/antigravity/antigravity-original "$@"
else
    exec /usr/share/antigravity/antigravity-original --no-sandbox --remote-debugging-port=9333 "$@"
fi

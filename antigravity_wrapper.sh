#!/bin/bash
if [[ "$*" == *"--type="* ]]; then
    exec /usr/share/antigravity/antigravity-original "$@"
else
    exec /usr/share/antigravity/antigravity-original --no-sandbox --remote-debugging-port=9333 "$@"
fi

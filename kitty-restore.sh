#!/usr/bin/env bash
# Convert the kitty dump JSON file into a kitty session file:
cat ~/.kitty-dump.json | python3 ~/scripts/kitty-convert-dump.py > ~/.kitty-session.kitty
# Start kitty from that session file:
kitty --single-instance --session ~/.kitty-session.kitty
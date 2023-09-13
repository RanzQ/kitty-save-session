#!/usr/bin/env bash
# Dump the current kitty session:
kitty @ ls > ~/.kitty-dump.json

# Restrict access to it
chmod 600 ~/.kitty-dump.json

# Convert the kitty dump JSON file into a kitty session file:
cat ~/.kitty-dump.json | python3 ~/scripts/kitty-convert-dump.py > ~/.kitty-session.kitty

# Delete the json
rm ~/.kitty-dump.json

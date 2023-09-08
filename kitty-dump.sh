#!/usr/bin/env bash
# Dump the current kitty session:
kitty @ ls > ~/.kitty-dump.json
# Restrict access to it
chmod 600 ~/.kitty-dump.json

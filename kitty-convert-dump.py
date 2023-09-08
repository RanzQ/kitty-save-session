#!/usr/bin/env python3
"""
this tool is used to convert Kitty session dump to Kitty session file which can be loaded by Kitty
"""

import json
import os
import sys

SHELL = os.getenv("SHELL")

def env_to_str(env):
    """Convert an env list to a series of '--env key=value' parameters and return as a string."""
    s = ""
    for key in env:
        s += f"--env {key}={env[key]} "

    return s.strip()


def cmdline_to_str(cmdline):
    """Convert a cmdline list to a space separated string."""
    s = ""
    for e in cmdline:
        s += f"{e} "

    return s.strip()


def fg_proc_to_str(fg):
    """Convert a foreground_processes list to a space separated string."""
    s = ""

    if len(fg) < 1:
        return s

    first_process = fg[0]

    s += f"{cmdline_to_str(first_process['cmdline'])}"

    # avoid re-launching kitty or kitty controls (like kitty-dump.sh or kitty @ ls)
    if 'kitty' in s:
        return SHELL
    return s


def convert(session):
    """Convert a kitty session dict, into a kitty session file and output it."""
    first = True
    for os_window in session:
        if first:
            first = False
        else:
            print("\nnew_os_window")

        for tab in os_window["tabs"]:
            print("\nnew_tab")
            print(f"layout {tab['layout']}")

            for w in tab["windows"]:
                print(f"cd {w['cwd']}")
                print(
                    f"launch {SHELL}"
                )
                if w["is_focused"]:
                    print("focus")


if __name__ == "__main__":
    stdin = sys.stdin.readlines()
    session = json.loads("".join(stdin))
    convert(session)


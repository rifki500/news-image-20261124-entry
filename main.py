#!/usr/bin/env python3
"""Entry for make.fun news-image-20261124.

Copies the pre-rendered newspaper image (entry.png, built by the agent
from Tuesday 24 November 2026 reporting) to the output directory.
Standard library only; no network; deterministic.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.png"),
        os.path.join(out_dir, "entry.png"),
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

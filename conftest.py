#!/usr/bin/env python3

"""Pytest configuration for repository-local imports."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

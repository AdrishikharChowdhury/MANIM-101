#!/bin/bash
cd "$(dirname "$0")/.."
.venv/bin/python -m manim -pqh src/wv_outro/__init__.py "$@"

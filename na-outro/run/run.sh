#!/bin/bash
cd "$(dirname "$0")/.."
.venv/bin/python -m manim -pqh src/na_outro/__init__.py "$@"

#!/bin/bash
cd "$(dirname "$0")/.."
.venv/bin/python -m manim -pqh src/rrs_intro/__init__.py "$@"

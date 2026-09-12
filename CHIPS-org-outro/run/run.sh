#!/bin/bash
cd "$(dirname "$0")/.."
.venv/bin/python -m manim -pqh main.py "$@"

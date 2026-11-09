#!/bin/bash
cd "$(dirname "$0")/.."
.venv/bin/python -m manim -pqh src/sql_crime_intro/__init__.py "$@"

@echo off
cd /d "%~dp0.."
.venv\Scripts\python -m manim -pqh main.py %*
pause

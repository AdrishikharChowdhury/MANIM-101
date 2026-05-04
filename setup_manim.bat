@echo off
set /p foldername="Enter project folder name: "

:: Create and move into the directory
mkdir %foldername%
cd %foldername%

:: Initialize the uv project
echo Initializing uv...
call uv init

:: Create the virtual environment
echo Creating virtual environment...
call uv venv

:: Activate the environment and install Manim
:: We use 'call' to ensure the script continues after activation
echo Installing Manim...
call .venv\Scripts\activate && uv add manim

echo.
echo Setup complete! Your project "%foldername%" is ready.
pause
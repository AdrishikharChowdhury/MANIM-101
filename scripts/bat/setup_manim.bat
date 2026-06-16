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

:: Create the run script
echo Creating run script...
(
echo @echo off
echo .venv\Scripts\python -m manim -pqh main.py %%*
echo pause
) > run.bat

echo.
echo Setup complete! Your project "%foldername%" is ready.
echo Use run.bat inside the folder to compile and preview.
pause
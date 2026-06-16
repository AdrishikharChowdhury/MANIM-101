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

:: Create the run folder and scripts
echo Creating run scripts...
mkdir run
(
echo @echo off
echo cd /d "%%~dp0.."
echo .venv\Scripts\python -m manim -pqh main.py %%*
echo pause
) > run\run.bat

echo.
echo Setup complete! Your project "%foldername%" is ready.
echo Use run\run.bat to compile and preview.
pause
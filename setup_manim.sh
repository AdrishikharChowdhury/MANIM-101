#!/bin/bash

# Prompt user for folder name
echo "Enter project folder name:"
read foldername

# Create and move into the directory
mkdir -p "$foldername"
cd "$foldername" || exit

# Initialize the uv project
echo "Initializing uv..."
uv init

# Create the virtual environment
echo "Creating virtual environment..."
uv venv

# Activate the environment and install Manim
# On Linux/macOS, the path is .venv/bin/activate
echo "Installing Manim..."
source .venv/bin/activate && uv add manim

echo ""
echo "Setup complete! Your project '$foldername' is ready."
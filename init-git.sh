#!/bin/bash

# Script to initialize a git repository for the DuckDuckGo CLI project

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Error: git is not installed. Please install git first."
    exit 1
fi

# Check if git user is configured
if [[ -z "$(git config --global user.name)" ]] || [[ -z "$(git config --global user.email)" ]]; then
    echo "Git user not configured. Please set your git credentials:"
    echo "  git config --global user.name \"Your Name\""
    echo "  git config --global user.email \"your.email@example.com\""
    echo ""
    echo "After setting your credentials, run this script again."
    exit 1
fi

# Navigate to the project directory
cd /home/alex/Documents/duckduckgo-cli

# Initialize git repository
git init

# Create initial commit
git add .
git commit -m "Initial commit: DuckDuckGo CLI v1.0.0"

echo "Git repository initialized successfully!"
echo ""
echo "To add a remote repository (e.g., GitHub):"
echo "1. Create a new repository on GitHub (or other git hosting service)"
echo "2. Uncomment and modify the following lines in this script:"
echo "   # git remote add origin <repository-url>"
echo "   # git branch -M main"
echo "   # git push -u origin main"
echo ""
echo "Example for GitHub:"
echo "   git remote add origin https://github.com/yourusername/duckduckgo-cli.git"
echo "   git branch -M main"
echo "   git push -u origin main"
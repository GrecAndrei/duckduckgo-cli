#!/bin/bash

# Script to make the DuckDuckGo CLI tool available system-wide

# Create a symlink in ~/bin if it doesn't exist
mkdir -p ~/bin
ln -sf /home/alex/Documents/duckduckgo-cli/ddgs ~/bin/ddg-cli

# Add to PATH if not already there
if [[ ":$PATH:" != *":$HOME/bin:"* ]]; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.profile
    echo "Added ~/bin to PATH. Please restart your terminal or run 'source ~/.bashrc' to apply changes."
fi

echo "DuckDuckGo CLI tool is now available as 'ddg-cli'"
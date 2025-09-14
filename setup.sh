#!/bin/bash

# Setup script for DuckDuckGo CLI

# Create directories if they don't exist
mkdir -p ~/bin
mkdir -p ~/.config/duckduckgo-cli

# Create symlinks
ln -sf /home/alex/Documents/duckduckgo-cli/ddgs ~/bin/ddg-cli

# Add to PATH if not already there
if [[ ":$PATH:" != *":$HOME/bin:"* ]]; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.profile
fi

# Install required dependencies
source /home/alex/Documents/ddg_search_env/bin/activate
pip install requests

echo "DuckDuckGo CLI setup complete!"
echo "You can now use the tool with the command: ddg-cli"
echo "Note: You may need to restart your terminal or run 'source ~/.bashrc' for the changes to take effect."
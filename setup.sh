#!/bin/bash

# Setup script for DuckDuckGo CLI

# Get the current directory (where the script is located)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Setting up DuckDuckGo CLI..."

# Create directories if they don't exist
mkdir -p ~/bin
mkdir -p ~/.config/duckduckgo-cli

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -r "$SCRIPT_DIR/requirements.txt"

# Make the main script executable
chmod +x "$SCRIPT_DIR/ddgs"

# Create a wrapper script in ~/bin
cat > ~/bin/ddg-cli << EOF
#!/bin/bash
# DuckDuckGo CLI wrapper script
export PYTHONPATH="$SCRIPT_DIR/src:\$PYTHONPATH"
python3 "$SCRIPT_DIR/ddgs" "\$@"
EOF

chmod +x ~/bin/ddg-cli

# Add ~/bin to PATH if not already there
if [[ ":$PATH:" != *":$HOME/bin:"* ]]; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.profile
fi

echo ""
echo "✅ DuckDuckGo CLI setup complete!"
echo ""
echo "You can now use the tool with the command: ddg-cli"
echo "Examples:"
echo "  ddg-cli search 'python programming'"
echo "  ddg-cli search 'machine learning' --results 20"
echo "  ddg-cli history list"
echo ""
echo "Note: You may need to restart your terminal or run 'source ~/.bashrc' for the PATH changes to take effect."
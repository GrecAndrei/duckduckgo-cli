#!/bin/bash

# Installation script for DuckDuckGo CLI

# Get the current directory (where the script is located)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Installing DuckDuckGo CLI system-wide..."

# Create a symlink in ~/bin if it doesn't exist
mkdir -p ~/bin

# Create a wrapper script instead of direct symlink to handle PYTHONPATH
cat > ~/bin/ddg-cli << EOF
#!/bin/bash
# DuckDuckGo CLI wrapper script
export PYTHONPATH="$SCRIPT_DIR/src:\$PYTHONPATH"
python3 "$SCRIPT_DIR/ddgs" "\$@"
EOF

chmod +x ~/bin/ddg-cli

# Add to PATH if not already there
if [[ ":$PATH:" != *":$HOME/bin:"* ]]; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.profile
    echo "Added ~/bin to PATH. Please restart your terminal or run 'source ~/.bashrc' to apply changes."
fi

echo "✅ DuckDuckGo CLI tool is now available as 'ddg-cli'"
echo "Try: ddg-cli search 'hello world'"
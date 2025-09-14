# DuckDuckGo CLI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A feature-rich command-line interface for DuckDuckGo search that brings the power of privacy-focused searching directly to your terminal. Whether you're a developer looking for quick documentation, a researcher gathering information, or someone who prefers the efficiency of command-line tools, this CLI has you covered.

<!-- Demo GIF would go here in a real repository -->
> **Note**: This tool works entirely in your terminal - no browser required! Perfect for server environments, automated scripts, or when you just want fast, private search results.

## Why Use DuckDuckGo CLI?

- **Privacy First**: Built on DuckDuckGo's privacy-focused search engine
- **Lightning Fast**: Get search results without opening a browser
- **Developer Friendly**: Export results in multiple formats for further processing
- **Highly Configurable**: Filter, bookmark, and organize your searches
- **Terminal Native**: Fits perfectly into any command-line workflow
- **Zero Tracking**: No personal data collection or search history stored externally

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Make the script executable
chmod +x ddgs

# Search for something
PYTHONPATH=./src python3 ddgs search "python web scraping"

# Get more results
PYTHONPATH=./src python3 ddgs search "machine learning tutorials" --results 20

# Export to JSON for processing
PYTHONPATH=./src python3 ddgs search "api documentation" --format json --output results.json
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/GrecAndrei/duckduckgo-cli.git
   cd duckduckgo-cli
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the tool (optional)**
   ```bash
   chmod +x ddgs
   ./setup.sh  # Creates system-wide symlink
   ```

After setup, you can use `ddg-cli` from anywhere in your terminal.

## Core Features

### 🔍 Smart Search
Search DuckDuckGo with customizable result counts and instant terminal output.

```bash
# Basic search
ddg-cli search "kubernetes deployment strategies"

# Limit results
ddg-cli search "react hooks examples" --results 5

# Quick search (backward compatibility)
ddg-cli "neural networks" 10
```

### 📊 Multiple Export Formats
Export your search results in the format that works best for your workflow.

```bash
# JSON for data processing
ddg-cli search "python libraries 2024" --format json --output libraries.json

# CSV for spreadsheet analysis
ddg-cli search "startup funding rounds" --format csv --output funding.csv

# Markdown for documentation
ddg-cli search "git best practices" --format markdown --output git-guide.md

# XML for structured data
ddg-cli search "weather api services" --format xml --output weather-apis.xml
```

### 🔧 Advanced Filtering
Fine-tune your search results with powerful filtering options.

```bash
# Include only GitHub repositories
ddg-cli search "javascript frameworks" --filter "github.com"

# Exclude tutorial content
ddg-cli search "machine learning" --exclude "tutorial"

# Combine for precise results
ddg-cli search "docker" --filter "documentation" --exclude "tutorial"
```

### 📚 Search History
Keep track of your searches and never lose that perfect query again.

```bash
# View your search history
ddg-cli history list

# Clear old searches
ddg-cli history clear
```

### 🔖 Bookmark Management
Save your most useful search queries for quick access.

```bash
# Bookmark a search
ddg-cli bookmarks add "python performance optimization"

# View all bookmarks
ddg-cli bookmarks list

# Clean up bookmarks
ddg-cli bookmarks clear
```

### 🌐 Browser Integration
Seamlessly move from terminal to browser when needed.

```bash
# Open all results in browser
ddg-cli search "new web technologies 2024" --open

# Download content for offline reading
ddg-cli search "programming cheatsheets" --download
```

## Real-World Examples

### For Developers
```bash
# Find API documentation
ddg-cli search "stripe api documentation" --filter "stripe.com" --format json

# Research new libraries
ddg-cli search "python async libraries" --results 15 --exclude "tutorial"

# Quick reference lookup
ddg-cli search "sql join syntax examples" --results 5
```

### For Researchers
```bash
# Academic research with export
ddg-cli search "climate change 2024 research" --format csv --output climate-research.csv

# News gathering
ddg-cli search "renewable energy news" --filter "2024" --results 25

# Fact-checking sources
ddg-cli search "vaccination statistics WHO" --filter "who.int"
```

### For Content Creators
```bash
# Topic research
ddg-cli search "content marketing trends 2024" --format markdown --output trends.md

# Competitor analysis
ddg-cli search "blog monetization strategies" --exclude "course"

# Social media research
ddg-cli search "instagram algorithm updates" --results 10 --open
```

## Command Reference

### Search Command
```
ddg-cli search <query> [options]

Options:
  -r, --results NUM     Number of results (default: 10)
  -f, --format FORMAT   Output format: text, json, csv, xml, markdown
  -o, --output FILE     Save results to file
  --filter TERM         Include only results containing term
  --exclude TERM        Exclude results containing term
  --open               Open URLs in browser
  --download           Download content from URLs
```

### History Commands
```
ddg-cli history list    # Show search history
ddg-cli history clear   # Clear search history
```

### Bookmark Commands
```
ddg-cli bookmarks add <query>    # Add bookmark
ddg-cli bookmarks list           # Show bookmarks
ddg-cli bookmarks clear          # Clear bookmarks
```

## Configuration

The CLI automatically creates a configuration file at `~/.ddgs_config.ini` with sensible defaults. You can customize:

- Default number of results
- Default output format
- Network timeout settings
- Display preferences

## Project Structure

This project is well-organized for easy maintenance and extension:

```
duckduckgo-cli/
├── ddgs                    # Main executable
├── src/                    # Core modules
│   ├── search.py          # DuckDuckGo search integration
│   ├── display.py         # Result formatting
│   ├── history.py         # Search history management
│   ├── bookmarks.py       # Bookmark system
│   ├── config.py          # Configuration management
│   ├── export.py          # Multi-format export
│   ├── filter.py          # Result filtering
│   └── utils.py           # Browser and download utilities
├── tests/                  # Test suite
└── docs/                   # Additional documentation
```

## Testing

Run the comprehensive test suite to ensure everything works correctly:

```bash
# Run all tests
PYTHONPATH=./src python3 tests/test_ddgs.py

# Or use make
make test
```

## Troubleshooting

### Common Issues

**"Module not found" errors**
```bash
# Ensure PYTHONPATH is set correctly
export PYTHONPATH="./src:$PYTHONPATH"
```

**Network connectivity issues**
- Check your internet connection
- Some networks may block DuckDuckGo search API
- Try using a VPN if searches consistently fail

**Permission denied on installation**
```bash
# Make scripts executable
chmod +x ddgs setup.sh install.sh
```

### Getting Help

If you encounter issues:
1. Check the [existing issues](../../issues) on GitHub
2. Review the troubleshooting section above
3. Create a new issue with details about your environment and the problem

## Performance Tips

- **Optimize result counts**: Use `--results` to limit output for faster searches
- **Use filters early**: Apply `--filter` and `--exclude` to reduce processing time
- **Export large datasets**: Use `--format json` for further processing with tools like `jq`
- **Bookmark frequent searches**: Save common queries to avoid retyping

## Advanced Usage

### Combining with Other Tools

```bash
# Process results with jq
ddg-cli search "api tutorials" --format json | jq '.[] | .title'

# Count results
ddg-cli search "python" --format json | jq '. | length'

# Extract URLs only
ddg-cli search "documentation" --format json | jq -r '.[].href'

# Filter and pipe to other commands
ddg-cli search "github repositories" --filter "python" --format csv | head -10
```

### Scripting Examples

```bash
#!/bin/bash
# Daily tech news aggregator
ddg-cli search "tech news $(date +'%Y')" --results 20 --format json > daily_tech.json

# Research automation
for topic in "kubernetes" "docker" "terraform"; do
    ddg-cli search "$topic best practices" --format markdown --output "${topic}_practices.md"
done
```

## API and Library Usage

While primarily a CLI tool, the modular architecture makes it easy to import individual components:

```python
from src.search import search_duckduckgo
from src.filter import filter_results

results = search_duckduckgo("python programming", 10)
filtered = filter_results(results, include="github.com")
```

## Contributing

We welcome contributions! Whether it's bug fixes, new features, or documentation improvements, your help makes this tool better for everyone.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines on:
- Setting up the development environment
- Code style and standards
- Testing requirements
- Submitting pull requests

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with the excellent [ddgs](https://pypi.org/project/ddgs/) library
- Inspired by the need for privacy-focused search tools
- Thanks to the DuckDuckGo team for providing a great search API

---

**Happy searching! 🦆**
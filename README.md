# DuckDuckGo CLI

A powerful command-line interface for searching DuckDuckGo with advanced features.

## Features

- Search DuckDuckGo with customizable result counts
- Multiple output formats (JSON, CSV, XML, Markdown, Text)
- Result filtering and exclusion capabilities
- Search history management
- Bookmark management
- Result export to files
- URL opening in browser
- Content downloading from URLs

## Installation

The tool is installed in `/home/alex/Documents/duckduckgo-cli/` and is available system-wide as `ddg-cli`.

## Usage

### Basic Search
```
ddg-cli search "Python programming"
ddg-cli search "machine learning" --results 20
```

### Export Results
```
ddg-cli search "Python" --format json --output results.json
ddg-cli search "Python" --format csv --output results.csv
```

### Filter Results
```
ddg-cli search "Python" --filter "github.com"
ddg-cli search "Python" --exclude "tutorial"
```

### Manage History
```
ddg-cli history list
ddg-cli history clear
```

### Manage Bookmarks
```
ddg-cli bookmarks add "Python programming"
ddg-cli bookmarks list
ddg-cli bookmarks clear
```

## Documentation

For more detailed information, see:
- [SUMMARY.md](SUMMARY.md) - Implementation summary
- [FINAL_SUMMARY.md](FINAL_SUMMARY.md) - Final implementation summary

## Testing

Run the test suite with:
```
cd /home/alex/Documents/duckduckgo-cli
./tests/test_ddgs.py
```
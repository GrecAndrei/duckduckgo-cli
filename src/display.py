"""
Display module for the enhanced ddgs tool with rich formatting support
"""

import json
import sys
from rich.console import Console
from rich.table import Table
from rich.text import Text

# Initialize console with fallback support
console = Console()

def display_results(results):
    """Display search results in a formatted way using rich tables."""
    if not results:
        console.print("No results found.", style="yellow")
        return

    # Check if we can use rich formatting (terminal supports it)
    if console.is_terminal and not sys.stdout.isatty():
        # Fallback to plain text for non-interactive environments
        _display_results_plain(results)
        return
    
    # Create a rich table
    table = Table(title="Search Results", show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=3)
    table.add_column("Title", style="bold green", min_width=30)
    table.add_column("URL", style="cyan", min_width=25)
    table.add_column("Snippet", style="dim", min_width=40)

    for i, result in enumerate(results, 1):
        title = Text(result.get('title', 'No title'))
        url = Text(result.get('href', 'No URL'))
        snippet = Text(result.get('body', 'No snippet'))
        
        # Truncate snippet if too long
        if len(snippet.plain) > 100:
            snippet = Text(snippet.plain[:97] + "...")
        
        table.add_row(str(i), title, url, snippet)

    console.print(table)

def _display_results_plain(results):
    """Fallback plain text display for non-supporting terminals."""
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['title']}")
        print(f"   URL: {result['href']}")
        print(f"   Snippet: {result['body']}")
        print()

def format_results(results, format_type):
    """Format results in the specified format."""
    if format_type == "json":
        return json.dumps(results, indent=2)
    else:
        # Default to text format
        output = []
        for i, result in enumerate(results, 1):
            output.append(f"{i}. {result['title']}")
            output.append(f"   URL: {result['href']}")
            output.append(f"   Snippet: {result['body']}")
            output.append("")
        return "\n".join(output)

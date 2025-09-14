"""
Display module for the enhanced ddgs tool
"""

import json

def display_results(results):
    """Display search results in a formatted way."""
    if not results:
        print("No results found.")
        return

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

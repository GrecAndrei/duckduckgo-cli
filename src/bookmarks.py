"""
Bookmarks module for the enhanced ddgs tool
"""

import json
import os
from pathlib import Path

class BookmarkManager:
    def __init__(self, bookmarks_file=None):
        if bookmarks_file is None:
            self.bookmarks_file = Path.home() / '.ddgs_bookmarks.json'
        else:
            self.bookmarks_file = Path(bookmarks_file)
        
        # Create bookmarks file if it doesn't exist
        if not self.bookmarks_file.exists():
            self.bookmarks_file.write_text('[]')
    
    def add_bookmark(self, query):
        """Add a query to bookmarks."""
        bookmarks = self.load_bookmarks()
        if query not in bookmarks:
            bookmarks.append(query)
            self.save_bookmarks(bookmarks)
            print(f"Bookmark added: {query}")
        else:
            print(f"Query already bookmarked: {query}")
    
    def load_bookmarks(self):
        """Load bookmarks from file."""
        try:
            return json.loads(self.bookmarks_file.read_text())
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def save_bookmarks(self, bookmarks):
        """Save bookmarks to file."""
        self.bookmarks_file.write_text(json.dumps(bookmarks, indent=2))
    
    def list_bookmarks(self):
        """List bookmarks."""
        bookmarks = self.load_bookmarks()
        if not bookmarks:
            print("No bookmarks found.")
            return
        
        print("Bookmarks:")
        for i, query in enumerate(bookmarks, 1):
            print(f"{i}. {query}")
    
    def clear_bookmarks(self):
        """Clear bookmarks."""
        self.bookmarks_file.write_text('[]')
        print("Bookmarks cleared.")
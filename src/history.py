"""
History module for the enhanced ddgs tool
"""

import json
import os
from datetime import datetime
from pathlib import Path

class HistoryManager:
    def __init__(self, history_file=None):
        if history_file is None:
            self.history_file = Path.home() / '.ddgs_history.json'
        else:
            self.history_file = Path(history_file)
        
        # Create history file if it doesn't exist
        if not self.history_file.exists():
            self.history_file.write_text('[]')
    
    def add_to_history(self, query, result_count):
        """Add a search query to history."""
        history = self.load_history()
        history.append({
            'query': query,
            'timestamp': datetime.now().isoformat(),
            'result_count': result_count
        })
        self.save_history(history)
    
    def load_history(self):
        """Load search history from file."""
        try:
            return json.loads(self.history_file.read_text())
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def save_history(self, history):
        """Save search history to file."""
        self.history_file.write_text(json.dumps(history, indent=2))
    
    def list_history(self):
        """List search history."""
        history = self.load_history()
        if not history:
            print("No search history found.")
            return
        
        print("Search History:")
        for i, entry in enumerate(history, 1):
            print(f"{i}. {entry['query']} (Results: {entry['result_count']}) - {entry['timestamp']}")
    
    def clear_history(self):
        """Clear search history."""
        self.history_file.write_text('[]')
        print("Search history cleared.")
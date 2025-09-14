#!/home/alex/Documents/ddg_search_env/bin/python3

"""
Test script for the enhanced ddgs tool
"""

import sys
import os

# Add the project directory to the Python path
sys.path.insert(0, '/home/alex/Documents/ddgs_enhanced/src')

# Test imports
try:
    from search import search_duckduckgo
    from display import display_results, format_results
    from history import HistoryManager
    from bookmarks import BookmarkManager
    from config import ConfigManager
    from export import export_results
    from filter import filter_results
    from utils import open_urls, download_content
    
    print("All modules imported successfully!")
    
    # Test search functionality
    print("\nTesting search functionality...")
    results = search_duckduckgo("Python programming", 5)
    print(f"Found {len(results)} results")
    
    # Test display functionality
    print("\nTesting display functionality...")
    display_results(results[:2])  # Display first 2 results
    
    # Test formatting
    print("\nTesting JSON formatting...")
    json_output = format_results(results[:2], 'json')
    print(json_output[:100] + "..." if len(json_output) > 100 else json_output)
    
    # Test history manager
    print("\nTesting history manager...")
    history_manager = HistoryManager()
    history_manager.add_to_history("Python programming", len(results))
    print("Added search to history")
    
    # Test bookmark manager
    print("\nTesting bookmark manager...")
    bookmark_manager = BookmarkManager()
    bookmark_manager.add_bookmark("Python programming")
    print("Added bookmark")
    
    # Test configuration manager
    print("\nTesting configuration manager...")
    config_manager = ConfigManager()
    config = config_manager.load_config()
    print(f"Default results: {config.get('general', 'default_results')}")
    
    print("\nAll tests passed!")
    
except Exception as e:
    print(f"Error during testing: {e}")
    import traceback
    traceback.print_exc()
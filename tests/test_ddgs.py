#!/usr/bin/env python3

"""
Test script for the enhanced ddgs tool
"""

import sys
import os
import pytest
from pathlib import Path

# Get the directory where this script is located and add src to path
SCRIPT_DIR = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(SCRIPT_DIR / "src"))

# Test imports
from search import search_duckduckgo
from display import display_results, format_results
from history import HistoryManager
from bookmarks import BookmarkManager
from config import ConfigManager
from export import export_results
from filter import filter_results
from utils import open_urls, download_content


def test_imports():
    """Test that all modules can be imported successfully."""
    # If we reach this point, imports were successful
    assert True


def test_search_functionality():
    """Test search functionality."""
    results = search_duckduckgo("Python programming", 5)
    assert len(results) > 0
    assert len(results) <= 5
    
    # Check that results have expected structure
    for result in results:
        assert 'title' in result
        assert 'href' in result
        assert 'body' in result  # The actual field name is 'body', not 'snippet'


def test_display_functionality():
    """Test display functionality."""
    # Create test results
    test_results = [
        {
            'title': 'Test Title',
            'href': 'https://example.com',
            'body': 'Test body content'  # Use 'body' instead of 'snippet'
        }
    ]
    
    # Test that display_results doesn't crash
    try:
        display_results(test_results)
        assert True
    except Exception:
        assert False, "display_results should not raise exceptions"


def test_formatting():
    """Test result formatting."""
    test_results = [
        {
            'title': 'Test Title',
            'href': 'https://example.com',
            'body': 'Test body content'  # Use 'body' instead of 'snippet'
        }
    ]
    
    json_output = format_results(test_results, 'json')
    assert isinstance(json_output, str)
    assert 'Test Title' in json_output


def test_history_manager():
    """Test history manager functionality."""
    history_manager = HistoryManager()
    
    # Test adding to history
    try:
        history_manager.add_to_history("Python programming", 5)
        assert True
    except Exception:
        assert False, "add_to_history should not raise exceptions"


def test_bookmark_manager():
    """Test bookmark manager functionality."""
    bookmark_manager = BookmarkManager()
    
    # Test adding bookmark
    try:
        bookmark_manager.add_bookmark("Python programming")
        assert True
    except Exception:
        assert False, "add_bookmark should not raise exceptions"


def test_configuration_manager():
    """Test configuration manager."""
    config_manager = ConfigManager()
    config = config_manager.load_config()
    
    # Check that config has expected sections
    assert config.has_section('general')
    assert config.get('general', 'default_results') == '10'


if __name__ == "__main__":
    # If run directly, run tests with output
    pytest.main([__file__, "-v"])
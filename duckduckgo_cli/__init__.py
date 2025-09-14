"""
DuckDuckGo CLI Package
"""

from .search import search_duckduckgo
from .display import display_results, format_results
from .history import HistoryManager
from .bookmarks import BookmarkManager
from .config import ConfigManager
from .export import export_results
from .filter import filter_results
from .utils import open_urls, download_content

__version__ = "1.2.0"
__all__ = [
    "search_duckduckgo",
    "display_results", 
    "format_results",
    "HistoryManager",
    "BookmarkManager", 
    "ConfigManager",
    "export_results",
    "filter_results",
    "open_urls",
    "download_content"
]
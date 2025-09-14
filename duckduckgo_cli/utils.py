"""
Utility module for the enhanced ddgs tool
"""

import webbrowser
import requests
import os
from pathlib import Path

def open_urls(urls):
    """Open URLs in the default browser."""
    for url in urls:
        webbrowser.open(url)

def download_content(urls, download_dir=None):
    """Download content from URLs."""
    if download_dir is None:
        download_dir = Path.home() / 'ddgs_downloads'
    
    # Create download directory if it doesn't exist
    download_dir.mkdir(parents=True, exist_ok=True)
    
    for url in urls:
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            # Extract filename from URL or use a default name
            filename = url.split('/')[-1] or 'downloaded_file'
            if '.' not in filename:
                filename += '.html'
            
            filepath = download_dir / filename
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {filepath}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")
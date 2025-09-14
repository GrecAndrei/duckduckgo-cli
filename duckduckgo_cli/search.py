"""
Search module for the enhanced ddgs tool
"""

try:
    from ddgs import DDGS
except ImportError:
    try:
        from duckduckgo_search import DDGS
    except ImportError:
        print("Error: Neither 'ddgs' nor 'duckduckgo-search' package is installed.")
        print("Please install one of them using pip:")
        print("  pip install ddgs")
        print("or")
        print("  pip install duckduckgo-search")
        exit(1)

def search_duckduckgo(query, max_results=10):
    """Perform a search on DuckDuckGo and return results."""
    results = []
    try:
        with DDGS() as ddgs:
            # Perform the search
            search_results = ddgs.text(query, max_results=max_results)
            for result in search_results:
                results.append({
                    'title': result['title'],
                    'href': result['href'],
                    'body': result['body']
                })
    except Exception as e:
        print(f"An error occurred during the search: {e}")
        return []
    
    return results
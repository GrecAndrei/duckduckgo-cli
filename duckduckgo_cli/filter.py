"""
Filter module for the enhanced ddgs tool
"""

def filter_results(results, include=None, exclude=None):
    """Filter results based on include/exclude criteria."""
    filtered = results
    
    if include:
        filtered = [r for r in filtered if include.lower() in r['title'].lower() or 
                                          include.lower() in r['href'].lower() or 
                                          include.lower() in r['body'].lower()]
    
    if exclude:
        filtered = [r for r in filtered if exclude.lower() not in r['title'].lower() and 
                                          exclude.lower() not in r['href'].lower() and 
                                          exclude.lower() not in r['body'].lower()]
    
    return filtered
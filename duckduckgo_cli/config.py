"""
Configuration module for the enhanced ddgs tool
"""

import configparser
import os
from pathlib import Path

class ConfigManager:
    def __init__(self, config_file=None):
        if config_file is None:
            # Use XDG standard configuration path
            self.config_file = Path.home() / ".config" / "duckduckgo-cli" / "config.ini"
            # Create directory if it doesn't exist
            self.config_file.parent.mkdir(parents=True, exist_ok=True)
        else:
            self.config_file = Path(config_file)
        
        # Default configuration
        self.default_config = {
            'general': {
                'default_results': '10',
                'default_format': 'text',
                'safe_search': '0'
            },
            'display': {
                'color_output': '1',
                'max_snippet_length': '200'
            },
            'network': {
                'timeout': '10',
                'retries': '3'
            }
        }
    
    def load_config(self):
        """Load configuration from file."""
        config = configparser.ConfigParser()
        
        # Set defaults
        for section, options in self.default_config.items():
            config.add_section(section)
            for key, value in options.items():
                config.set(section, key, value)
        
        # Load user config if it exists
        if self.config_file.exists():
            config.read(self.config_file)
        
        return config
    
    def save_config(self, config):
        """Save configuration to file."""
        with open(self.config_file, 'w') as f:
            config.write(f)
    
    def get_config_path(self):
        """Get the configuration file path."""
        return self.config_file
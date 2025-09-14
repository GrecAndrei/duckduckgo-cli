# Makefile for DuckDuckGo CLI

# Variables
PYTHON = python3
PIP = pip
PROJECT_DIR = /home/alex/Documents/duckduckgo-cli
VENV_DIR = /home/alex/Documents/ddg_search_env

# Default target
.PHONY: help
help:
	@echo "DuckDuckGo CLI Makefile"
	@echo "======================"
	@echo "Available targets:"
	@echo "  install     - Install the CLI tool system-wide"
	@echo "  test        - Run the test suite"
	@echo "  clean       - Clean up temporary files"
	@echo "  setup       - Set up the development environment"
	@echo "  help        - Show this help message"

# Install the CLI tool system-wide
.PHONY: install
install:
	@echo "Installing DuckDuckGo CLI system-wide..."
	$(PROJECT_DIR)/install.sh

# Run the test suite
.PHONY: test
test:
	@echo "Running test suite..."
	$(VENV_DIR)/bin/python $(PROJECT_DIR)/tests/test_ddgs.py

# Clean up temporary files
.PHONY: clean
clean:
	@echo "Cleaning up temporary files..."
	rm -f *.tmp *.log
	rm -rf __pycache__ */__pycache__

# Set up the development environment
.PHONY: setup
setup:
	@echo "Setting up development environment..."
	$(PROJECT_DIR)/setup.sh

# Run a basic search test
.PHONY: search-test
search-test:
	@echo "Running basic search test..."
	$(VENV_DIR)/bin/python $(PROJECT_DIR)/ddgs search "Python programming" --results 3
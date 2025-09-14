# Makefile for DuckDuckGo CLI

# Variables
PYTHON = python3
PIP = pip3
PROJECT_DIR = $(shell pwd)

# Default target
.PHONY: help
help:
	@echo "DuckDuckGo CLI Makefile"
	@echo "======================"
	@echo "Available targets:"
	@echo "  install     - Install the CLI tool system-wide"
	@echo "  setup       - Set up the development environment"
	@echo "  test        - Run the test suite"
	@echo "  clean       - Clean up temporary files"
	@echo "  help        - Show this help message"

# Install the CLI tool system-wide
.PHONY: install
install:
	@echo "Installing DuckDuckGo CLI system-wide..."
	$(PROJECT_DIR)/install.sh

# Set up the development environment
.PHONY: setup
setup:
	@echo "Setting up development environment..."
	$(PROJECT_DIR)/setup.sh

# Run the test suite
.PHONY: test
test:
	@echo "Running test suite..."
	$(PYTHON) $(PROJECT_DIR)/tests/test_ddgs.py

# Clean up temporary files
.PHONY: clean
clean:
	@echo "Cleaning up temporary files..."
	rm -f *.tmp *.log
	rm -rf __pycache__ */__pycache__
	rm -rf src/__pycache__

# Run a basic search test (will only work if network allows)
.PHONY: search-test
search-test:
	@echo "Running basic search test..."
	$(PROJECT_DIR)/ddgs search "Python programming" --results 3
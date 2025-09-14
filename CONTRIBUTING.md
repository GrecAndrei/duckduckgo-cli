# Contributing to DuckDuckGo CLI

Thank you for your interest in contributing to DuckDuckGo CLI! We welcome contributions from the community to help improve this tool.

## Getting Started

1. Fork the repository on GitHub
2. Clone your forked repository to your local machine
3. Create a new branch for your feature or bug fix
4. Make your changes
5. Test your changes thoroughly
6. Commit your changes with a clear and descriptive commit message
7. Push your changes to your forked repository
8. Submit a pull request to the main repository

## Development Setup

1. Ensure you have Python 3.x installed
2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Install the `ddgs` package:
   ```
   pip install ddgs
   ```

## Code Style

- Follow PEP 8 style guidelines for Python code
- Use clear and descriptive variable and function names
- Write docstrings for all functions and classes
- Keep functions small and focused on a single task
- Add comments to explain complex logic

## Testing

- Add tests for new features or bug fixes
- Ensure all existing tests pass before submitting a pull request
- Run the test suite with:
  ```
  cd /path/to/duckduckgo-cli
  ./tests/test_ddgs.py
  ```

## Documentation

- Update the README.md file if you add new features or change existing functionality
- Add comments to explain complex code
- Update the SUMMARY.md and FINAL_SUMMARY.md files if necessary

## Reporting Issues

If you find a bug or have a feature request, please open an issue on GitHub with:

1. A clear and descriptive title
2. A detailed description of the problem or feature request
3. Steps to reproduce the issue (if applicable)
4. Expected behavior vs. actual behavior
5. Any relevant error messages or logs

## Pull Request Guidelines

- Keep pull requests focused on a single feature or bug fix
- Include a clear and descriptive title
- Provide a detailed description of the changes
- Reference any related issues in the description
- Ensure all tests pass before submitting
- Be responsive to feedback during the review process

## Code of Conduct

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.

## Questions?

If you have any questions about contributing, feel free to open an issue or contact the maintainers directly.
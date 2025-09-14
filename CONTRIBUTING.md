# Contributing to DuckDuckGo CLI 🚀

Thank you for your interest in contributing to DuckDuckGo CLI! We're excited to have you as part of our community and welcome contributions of all sizes - from fixing typos to adding major features.

## 🌟 Getting Started

Contributing is easier than you might think! Here's how to get started:

1. **Fork the repository** on GitHub (there's a friendly "Fork" button at the top right)
2. **Clone your forked repository** to your local machine
3. **Create a new branch** for your feature or bug fix (`git checkout -b awesome-new-feature`)
4. **Make your changes** - don't worry about making them perfect initially!
5. **Test your changes** to make sure everything works
6. **Commit your changes** with a clear message (`git commit -m "Add awesome new feature"`)
7. **Push your changes** to your forked repository
8. **Submit a pull request** - we'll review it together!

## 🛠️ Development Setup

Setting up your development environment is straightforward:

### Prerequisites
- Python 3.8 or higher
- pip (usually comes with Python)

### Setup Steps
1. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -e .  # Install the package in development mode
   pip install pytest  # For running tests
   ```

3. **Verify installation**:
   ```bash
   ddg-cli --help  # Should show the help message
   ```

## 🧪 Testing

We value quality, but don't let testing intimidate you:

- **Run existing tests**: `python -m pytest tests/`
- **Add tests for new features** - even simple tests help!
- **Manual testing** is valuable too - try your changes with real searches

## 🎨 Code Style

We keep it simple and readable:

- Follow [PEP 8](https://pep8.org/) Python style guidelines
- Use clear, descriptive names for variables and functions
- Add docstrings to help others understand your code
- Don't worry about being perfect - we'll help polish things during review!

## 📖 Documentation

- Update README.md if you're adding user-facing features
- Add inline comments for complex logic
- Docstrings are appreciated but not required for small changes

## 🐛 Reporting Issues

Found a bug or have an idea? We'd love to hear about it!

**For bugs:**
- Describe what you expected vs. what happened
- Include the command you ran and any error messages
- Let us know your operating system and Python version

**For feature requests:**
- Describe the feature and why it would be useful
- Feel free to suggest implementation ideas, but don't worry if you're not sure

## 🤝 Pull Request Guidelines

- **One feature per PR** makes review easier
- **Describe your changes** - help us understand what you've built
- **Don't worry about perfection** - we're here to help improve things together
- **Be patient** - we'll review as soon as we can and provide constructive feedback

## 💬 Getting Help

Stuck? Have questions? We're here to help!

- Open an issue with your question
- Mark it with "question" label
- Don't hesitate to ask - there are no silly questions!

## ✨ Types of Contributions We Love

- 🐛 Bug fixes
- 🚀 New features
- 📚 Documentation improvements
- 🧪 Adding tests
- 🎨 UI/UX improvements
- 🔧 Performance improvements
- 💡 Ideas and suggestions

## 📜 Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code. We're committed to making this a welcoming, inclusive project for everyone.

---

**Remember**: Contributing to open source should be fun and rewarding. Don't stress about making everything perfect - we're all learning together! 🎉
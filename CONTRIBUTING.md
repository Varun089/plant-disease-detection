# Contributing to Plant Disease Detection

Thank you for your interest in contributing to the Plant Disease Detection project! This document provides guidelines and instructions for contributing.

## How to Contribute

### Reporting Bugs

Before creating a bug report, please check the issue list as you might find out that you don't need to create one. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps which reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and the expected behavior**
- **Explain why this enhancement would be useful**

## Development Setup

### Prerequisites
- Python 3.8 or higher
- Node.js 14 or higher
- Docker and Docker Compose (optional)

### Local Development

1. Fork the repository
2. Clone your forked repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/plant-disease-detection.git
   cd plant-disease-detection
   ```
3. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Set up backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
5. Set up frontend:
   ```bash
   cd frontend
   npm install
   ```

## Code Style Guidelines

### Python
- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Use type hints where applicable

### JavaScript/React
- Use ESLint configuration provided in the project
- Follow JavaScript Standard Style
- Use meaningful component and variable names
- Add comments for complex logic

## Commit Message Conventions

Use clear and descriptive commit messages:

```
type(scope): subject

body

footer
```

Types: feat, fix, docs, style, refactor, perf, test, chore

Examples:
- `feat(model): add CNN-LSTM architecture improvements`
- `fix(api): resolve sensor data parsing issue`
- `docs(readme): update installation instructions`

## Pull Request Process

1. Update README.md with any new features or changes
2. Ensure all tests pass locally
3. Update CHANGELOG.md if applicable
4. Create a pull request with a clear description of the changes
5. Link any related issues in the PR description
6. Ensure your PR has a clear title following commit conventions

## Testing

Before submitting a pull request:
- Test your changes thoroughly
- Ensure existing functionality is not broken
- Add tests for new functionality if applicable

## Questions or Need Help?

Feel free to reach out to us:
- **Project Lead**: Vikas Gangwar (vg.vikas@kiet.edu.in)
- **Team Members**: 
  - Sehaj Sachdeva (2300290120221)
  - Varun Sagar (2300290120278)
  - Yuvraj Singh (2300290120292)

## License

By contributing to this project, you agree that your contributions will be licensed under its MIT License.

## Recognition

All contributors will be recognized in the project's contributor list and CHANGELOG.

Thank you for contributing!

# 📦 pkgmngr

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)

A powerful CLI utility that streamlines the entire Python package lifecycle - from creation to publication. Built for modern Python development workflows, pkgmngr helps you create, document, manage, and share Python packages efficiently.

## Why pkgmngr?

Python package management involves repetitive and often tedious steps: setting up project structure, maintaining documentation, syncing with GitHub, handling version changes, publishing to PyPI, and more.

pkgmngr addresses these challenges with a streamlined workflow:

- **Save Time**: Automate repetitive setup and maintenance tasks
- **Standardize Structure**: Ensure consistent package layout across projects
- **Document Easily**: Create comprehensive markdown snapshots for documentation and context sharing
- **Collaborate Better**: Perfect for sharing code context with AI assistants and collaborators
- **Manage Lifecycle**: Seamlessly handle package renaming, version updates, and publication

## 🛠️ Installation

```bash
# Install from PyPI
pip install pkgmngr

# Or install from source
git clone https://github.com/B4PT0R/pkgmngr.git
cd pkgmngr
pip install -e .
```

## 🚀 Quick Start

```bash
# Install from PyPI
pip install pkgmngr

# Create a new package
pkgmngr new my-package
cd my-package

# Generate the package files
pkgmngr create

# Initialize Git and GitHub repositories (requires GITHUB_TOKEN)
pkgmngr init-repo

# Make some changes to your code...

# Take a snapshot of your project
pkgmngr snapshot -m "Initial implementation"

# Push changes to GitHub
pkgmngr push

# Publish to PyPI when ready
pkgmngr publish
```

## 📋 Features and Usage Guide

### 📝 Package Creation

```bash
# Create a new package directory with config file
pkgmngr new my-package

# Edit the generated config file (optional)
cd my-package
nano pkgmngr.toml

# Generate the package structure
pkgmngr create
```

This creates a complete package structure with:
- Python module files with proper imports
- Tests directory with pytest setup
- Setup.py and pyproject.toml with appropriate metadata
- README.md, LICENSE, and other standard files
- .gitignore with sensible defaults

The `create` command uses your `pkgmngr.toml` configuration file to generate a standardized package structure. You can customize aspects like author, version, dependencies, and Python version requirements in this file.

### 🔄 Package Wrapping

Already started coding but want to transform your code into a proper package structure? The `wrap` command helps with that:

```bash
# In a directory with existing Python files
pkgmngr wrap

# Specify a custom package name
pkgmngr wrap --name my-custom-package

# Auto-overwrite existing files
pkgmngr wrap --overwrite
```

What the `wrap` command does:
- Creates a proper package structure around your existing code
- Moves Python files into the main package directory
- Organizes test files into a tests/ directory
- Creates standard files (setup.py, README.md, LICENSE, etc.)
- Adds `__init__.py` files to create proper Python packages
- Preserves your existing code while providing a proper package structure

This is perfect when you've started with a prototype or script and want to transform it into a distributable package without disrupting your existing code.

### 📸 Package Snapshots

Create comprehensive code documentation snapshots with a single command:

```bash
# Create a snapshot with a comment
pkgmngr snapshot -m "Implemented core features"

# List all available snapshots
pkgmngr snapshot -l
```

Snapshots include:
- Visual directory structure with file type icons
- Navigable table of contents
- All file contents with proper syntax highlighting
- Metadata and comments

Snapshots are perfect for:
- Sharing code context with AI assistants
- Documenting code for team members
- Creating restoration points
- Providing self-contained project documentation

### 🔙 Snapshot Restoration

Easily restore your project to a previous state using snapshots:

```bash
# Restore from a specific snapshot (by number)
pkgmngr restore 1

# Interactively select files to restore
pkgmngr restore -i

# Restore only Python files
pkgmngr restore -p "*.py"

# Exclude certain files
pkgmngr restore -e "temp_*.py"
```

The restoration process automatically creates a backup of your current state before applying changes, allowing you to safely experiment with restoring different versions.

### 🔄 Configuration Updates

When you've modified your `pkgmngr.toml` configuration file, you can apply those changes with:

```bash
# Update package files to match current configuration
pkgmngr update

# Force updates without confirmation prompts
pkgmngr update --force
```

The `update` command:
- Regenerates setup.py to match current configuration
- Updates standard files that depend on config options (LICENSE)
- Renames the package directory if package name has changed
- Updates Git repository description
- Updates GitHub repository "About" section (if GITHUB_TOKEN is available)

### 📋 Rename Packages

Easily rename your package and automatically update all references:

```bash
# Rename a package (updates all references and directory structure)
pkgmngr rename new-package-name
```

This updates the package directory name, all references in your code, and even renames the GitHub repository if available.

### 🔍 Global Search & Replace

Safely perform search and replace operations across your entire codebase:

```bash
# Replace text across all files
pkgmngr replace "old_text" "new_text"

# Use regular expressions
pkgmngr replace --regex "function\s+old_name" "function new_name"

# Preview changes before applying
pkgmngr replace "old_text" "new_text" --no-preview
```

Includes preview mode, automatic backups, and selective file targeting for safety.

### 🔄 GitHub Integration

Seamlessly integrate with GitHub:

```bash
# Initialize Git and create GitHub repository
pkgmngr init-repo

# Push changes with an interactive commit message
pkgmngr push
```

To use GitHub integration, set up a GitHub Personal Access Token:

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate a new token with the `repo` scope
3. Set it as an environment variable:
   ```bash
   export GITHUB_TOKEN=your_token_here
   ```

### 📦 PyPI Publishing

Publish your package with automatic version increments:

```bash
# Publish to TestPyPI for testing
pkgmngr publish --test

# Publish to PyPI with automatic patch version increment
pkgmngr publish

# Publish with a specific version increment type
pkgmngr publish --bump minor
```

Before publishing, ensure you have configured your PyPI credentials using one of these methods:
- A `.pypirc` file in your home directory
- Environment variables: `TWINE_USERNAME` and `TWINE_PASSWORD`
- API tokens (recommended for security)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

This project is almost entirely coded by Claude 3.7 following my general outlines. As it began to be functional, pkgmngr was itself used to facilitate the process: take a snapshot, give it to Claude, suggest changes, Claude does the changes and updates tests, copy/paste to the actual codebase, run tests, push to github, publish once in a while, repeat...
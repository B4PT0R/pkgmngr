# pypkg

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)

A comprehensive Python package utility that streamlines creation, snapshotting, and lifecycle management of Python packages. Designed for modern Python development workflows, pypkg helps developers save time on repetitive setup tasks and enhances collaboration, including AI-assisted development.

## Why pypkg?

- **Save Time**: Automate repetitive package setup and maintenance tasks
- **Standardize Structure**: Ensure consistent package layout across projects
- **Simplify Collaboration**: Easily share code context with snapshots
- **Streamline Workflow**: Integrate with GitHub and PyPI in a few commands
- **Enhance AI Collaboration**: Create perfect context snapshots for AI assistants

## Features

### Package Creation
- **Zero Config Setup**: Create standard Python package structures with a single command
- **Templated Files**: Generate all necessary project files (setup.py, README.md, LICENSE, etc.)
- **Git Ready**: Initialize Git repositories with GitHub integration

### Package Snapshots
- **Code Documentation**: Create beautiful markdown snapshots of your entire codebase
- **AI Collaboration**: Perfect for sharing code context with AI assistants
- **Point-in-Time Recovery**: Restore from snapshots with precision control
- **Selective Restoration**: Choose specific files or patterns to restore

### Lifecycle Management
- **Package Evolution**: Rename packages and automatically update all references
- **GitHub Integration**: Push changes to GitHub with a single command
- **PyPI Publishing**: Publish packages to PyPI (or TestPyPI) with ease

## Installation

```bash
# Install from PyPI
pip install pypkg

# Or install from source
git clone https://github.com/B4PT0R/pypkg.git
cd pypkg
pip install -e .
```

## Quick Start

```bash
# Create a new package
pypkg new my-package
cd my-package

# Generate the package files
pypkg create

# Initialize Git and GitHub repositories (requires GITHUB_TOKEN)
pypkg init-repo

# Make some changes to your code...

# Take a snapshot of your project
pypkg snapshot -m "Initial implementation"

# Push changes to GitHub
pypkg push

# Publish to PyPI when ready
pypkg publish
```

## Detailed Usage Guide

### Creating a New Package

The `new` command creates a directory with a configuration file:

```bash
# Create a new package directory with config file
pypkg new my-package
```

Output:
```
✅ Created package directory and config file for 'my-package':
- my-package/pypkg.toml

To finish creating your package:
- Change to the project's directory: `cd my-package`
- Review and edit the config file in your favorite editor: e.g. `nano pypkg.toml`
- Then run `pypkg create` to generate the project files.
...
```

This creates a directory with a `pypkg.toml` configuration file. You can edit this file to customize package details before generating the actual structure.

```bash
# Navigate to the new directory
cd my-package

# Review and edit the config file (pypkg.toml)
# Then generate the package files
pypkg create
```

Output:
```
ℹ️ Creating package structure for 'my-package'...
Created directory: my_package
Created: my_package/__init__.py
Created: my_package/__main__.py
Created directory: tests
Created: tests/test_my_package.py
Created: tests/run_tests.py
Created: setup.py
Created: README.md
Created: MANIFEST.in
Created: pyproject.toml
Created: LICENSE
Created: .gitignore

Package successfully created with the following structure:
./
├── my_package/
│   ├── __init__.py
│   └── __main__.py
├── tests/
│   ├── test_my_package.py
│   └── run_tests.py
├── setup.py
├── README.md
├── MANIFEST.in
├── pyproject.toml
├── LICENSE
└── .gitignore

✅ Package created successfully!
```

The `create` command generates a standard Python package structure based on your configuration.

### GitHub Integration

Initialize Git and create a GitHub repository:

```bash
# Set your GitHub token as an environment variable
export GITHUB_TOKEN=your_github_token_here

# Initialize Git and GitHub repositories
pypkg init-repo
```

Output:
```
ℹ️ Detected GitHub repository: yourusername/my-package
ℹ️ Initialized empty Git repository
ℹ️ Created initial commit
ℹ️ Creating GitHub repository: yourusername/my-package...
✅ Created GitHub repository: yourusername/my-package
ℹ️ Pushing code to GitHub...
✅ Pushed code to GitHub: https://github.com/yourusername/my-package.git
✅ Repository initialization completed successfully!
```

### Taking Snapshots

Snapshots create comprehensive Markdown documentation of your codebase:

```bash
# Create a snapshot with a comment
pypkg snapshot -m "Implemented core features"

# List all available snapshots
pypkg snapshot -l
```

Output:
```
Available snapshots:
----------------------------------------------------------------------------------------------------
#   Type     Date                Filename                       Comment
----------------------------------------------------------------------------------------------------
1   SNAPSHOT 2025-03-10 15:30:45 snapshot_2025-03-10_15-30-45.md Implemented core features
----------------------------------------------------------------------------------------------------
```

Snapshots include:
- Directory structure with file type icons
- Navigable table of contents
- All file contents with proper syntax highlighting
- Metadata and comments

### Restoring from Snapshots

```bash
# Restore from a specific snapshot (by number)
pypkg restore 1

# Interactively select files to restore
pypkg restore -i

# Restore only Python files
pypkg restore -p "*.py"

# Exclude certain files
pypkg restore -e "temp_*.py"

# Specify restore mode (safe, overwrite, force)
pypkg restore 1 -m safe
```

Restoration modes:
- `safe`: Skips existing files
- `overwrite`: Replaces existing files (default)
- `force`: Replaces all files, including read-only

### Package Lifecycle Management

#### Renaming Packages

The `rename` command allows you to change your package name and automatically updates all references:

```bash
# Rename a package (and update all references)
pypkg rename old-package-name new-package-name
```

This command:
- Updates the package directory name (`old_name` → `new_name`)
- Updates imports in all Python files
- Renames test files to match the new package name
- Updates `setup.py` with the new package name
- Updates the README.md with the new name
- Updates the `pypkg.toml` configuration file

Output:
```
ℹ️ Updated config file with new package name: new-package-name
ℹ️ Renamed package directory: old_package_name → new_package_name
ℹ️ Renamed test file: tests/test_old_package_name.py → tests/test_new_package_name.py
ℹ️ Updated references in setup.py
ℹ️ Updated references in README.md
✅ Project successfully renamed from 'old-package-name' to 'new-package-name'
```

Example usage:
```bash
# Before: my-package (directory: my_package)
pypkg rename my-package awesome-package
# After: awesome-package (directory: awesome_package)
```

Note that this command must be run from the package root directory (where the `pypkg.toml` file is located).

#### GitHub and PyPI Management

```bash
# Push changes to GitHub (with interactive commit message)
pypkg push

# Publish to TestPyPI
pypkg publish --test

# Publish to PyPI
pypkg publish
```

## Configuration

The `pypkg.toml` file contains configuration settings for your package:

```toml
package_name = "my-package"
author = "Your Name"
year = "2025"
description = "A Python package named my-package"

[github]
username = "your-username"
private = false

[python]
requires = ">=3.6"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[dependencies]
requires = []
dev_requires = [
    "pytest",
    "pytest-cov",
    "flake8",
    "black",
]
```

## GitHub Personal Access Token

For GitHub integration, you'll need a GitHub Personal Access Token with the `repo` scope:

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate a new token with the `repo` scope
3. Set it as the `GITHUB_TOKEN` environment variable:
   ```bash
   export GITHUB_TOKEN=your_token_here
   ```

## Snapshot Features

### Beautiful Directory Tree

Snapshots include a visually enhanced directory tree with file type icons and proper hierarchy:

```
📦 my_project
├─ 📂 src
│  ├─ 🐍 __init__.py
│  ├─ 🐍 main.py
│  └─ 🐍 utils.py
├─ 📂 tests
│  ├─ 🐍 test_main.py
│  └─ 🐍 test_utils.py
├─ 📝 README.md
└─ 📋 requirements.txt
```

### Navigable Table of Contents

Each snapshot includes a clickable table of contents that links directly to file sections for easy navigation.

### Syntax Highlighting

Code sections are properly syntax-highlighted based on file extensions, making your snapshots readable and beautiful.

## Advanced Usage

### Custom Snapshot Paths

```bash
# Specify a different start path and output folder
pypkg snapshot /path/to/project -o custom_snapshots
```

### Gitignore Integration

Snapshots respect your `.gitignore` patterns, but also support special `#pypkg` prefixed patterns that only apply to snapshots:

```
# Regular .gitignore pattern (ignored by Git and snapshots)
__pycache__/

# Snapshot-specific pattern (ignored by snapshots only)
#pypkg secrets.json
```

### Automatic Backups

When restoring, a backup snapshot is automatically created:

```bash
# Restore without creating a backup
pypkg restore 1 --no-backup

# Specify a custom backup location
pypkg restore 1 -b /path/to/backup.md
```

## Troubleshooting

### Common Issues

1. **'pypkg' command not found**
   - Ensure the installation directory is in your PATH
   - Try installing with `pip install --user pypkg`

2. **GitHub authentication errors**
   - Check that your GITHUB_TOKEN environment variable is set correctly
   - Ensure your token has the 'repo' scope

3. **Snapshot restore fails**
   - Check if you have write permissions to all affected files
   - Try using the `-m force` option for stubborn files

### Getting Help

If you encounter any issues not covered here, please file an issue on GitHub: https://github.com/B4PT0R/pypkg/issues

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/B4PT0R/pypkg.git
cd pypkg

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e .[dev]
```

### Running Tests

```bash
pytest
# Or with coverage
pytest --cov=pypkg tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please make sure your code follows the existing style and passes all tests.

## License

MIT
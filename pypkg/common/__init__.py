"""
Common utilities module for pypkg.

This module provides shared functionality used by different components
of the pypkg package.
"""

from .utils import create_directory, sanitize_package_name
from .templates import get_gitignore_content
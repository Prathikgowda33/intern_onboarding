#!/usr/bin/env python3
"""File organizer — sorts files into subdirectories by extension category."""

import argparse
import os
import shutil
import sys

# Extension → category mapping. Modify if needed.
EXTENSION_MAP = {
    # Images
    ".jpg": "images", ".jpeg": "images", ".png": "images",
    ".gif": "images", ".svg": "images", ".webp": "images",
    # Documents
    ".pdf": "docs", ".doc": "docs", ".docx": "docs",
    ".txt": "docs", ".md": "docs", ".rtf": "docs",
    # Data
    ".csv": "data", ".json": "data", ".xml": "data",
    ".xlsx": "data", ".xls": "data",
    # Archives
    ".zip": "archives", ".tar": "archives", ".gz": "archives",
    ".rar": "archives", ".7z": "archives",
    # Code
    ".py": "code", ".js": "code", ".html": "code",
    ".css": "code", ".java": "code",
}


def parse_args():
    """Parse command-line arguments.

    Returns:
        argparse.Namespace: parsed arguments with `directory` and `dry_run` attributes.
    """
    parser = argparse.ArgumentParser(
        description="Organize files in a directory into subdirectories by extension."
    )
    parser.add_argument(
        "--directory", required=True, help="Path to the directory to organize."
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print what would happen without actually moving files."
    )
    return parser.parse_args()


def categorize(filename):
    """Determine the category for a file based on its extension.

    Args:
        filename (str): the file name (e.g., "photo.jpg").

    Returns:
        str: the category name (e.g., "images"), or None if the extension is unknown.
    """
    # TODO: implement
    pass


def create_category_dirs(base_dir, categories):
    """Create subdirectories for each category that doesn't already exist.

    Args:
        base_dir (str): the base directory path.
        categories (set): a set of category names to create.
    """
    # TODO: implement
    pass


def organize_files(directory, dry_run=False):
    """Scan the directory and move files into category subdirectories.

    Args:
        directory (str): the directory to organize.
        dry_run (bool): if True, print actions without moving files.
    """
    # TODO: implement
    pass


def main():
    """Entry point: parse args and run the organizer."""
    # TODO: implement
    pass


if __name__ == "__main__":
    main()

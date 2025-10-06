#!/usr/bin/env python3
"""
Script to fix markdown list formatting by ensuring all lists are preceded by a blank line.
Supports both .md and .qmd files and processes directories recursively.
"""

import os
import re
import argparse
from pathlib import Path


def fix_markdown_lists(content):
    """
    Fix markdown list formatting by ensuring lists are preceded by a blank line.

    Args:
        content (str): The markdown content to fix

    Returns:
        str: The fixed content
    """
    lines = content.split('\n')
    fixed_lines = []

    for i, line in enumerate(lines):
        # Check if current line is a list item (starts with -, *, +, or number.)
        is_list_item = re.match(r'^(\s*)[-*+]\s', line) or re.match(r'^(\s*)\d+\.\s', line)

        if is_list_item:
            # Check if this is not a nested list (no preceding list item)
            prev_line_idx = i - 1
            is_nested = False

            if prev_line_idx >= 0:
                prev_line = lines[prev_line_idx]
                # Check if previous line is also a list item or empty
                prev_is_list = re.match(r'^(\s*)[-*+]\s', prev_line) or re.match(r'^(\s*)\d+\.\s', prev_line)
                prev_is_empty = prev_line.strip() == ''

                if prev_is_list:
                    is_nested = True
                elif not prev_is_empty and prev_line_idx > 0:
                    # Check if there's already a blank line before
                    two_lines_back = lines[prev_line_idx - 1] if prev_line_idx > 0 else ''
                    if two_lines_back.strip() == '':
                        is_nested = True

            # If it's not nested and previous line is not empty, add blank line
            if not is_nested and i > 0 and lines[i-1].strip() != '':
                fixed_lines.append('')

        fixed_lines.append(line)

    return '\n'.join(fixed_lines)


def process_file(file_path):
    """
    Process a single markdown file.

    Args:
        file_path (Path): Path to the file to process

    Returns:
        bool: True if file was modified, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        fixed_content = fix_markdown_lists(original_content)

        if original_content != fixed_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"Fixed: {file_path}")
            return True
        else:
            print(f"No changes needed: {file_path}")
            return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def find_markdown_files(directory):
    """
    Recursively find all markdown files in a directory.

    Args:
        directory (Path): Directory to search

    Yields:
        Path: Markdown file paths
    """
    for file_path in directory.rglob('*'):
        if file_path.is_file() and file_path.suffix.lower() in ['.md', '.qmd']:
            yield file_path


def main():
    parser = argparse.ArgumentParser(
        description="Fix markdown list formatting by ensuring lists are preceded by blank lines"
    )
    parser.add_argument(
        'path',
        nargs='?',
        default='.',
        help='File or directory to process (default: current directory)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without making modifications'
    )

    args = parser.parse_args()

    path = Path(args.path)

    if not path.exists():
        print(f"Error: Path '{path}' does not exist")
        return 1

    files_to_process = []

    if path.is_file():
        if path.suffix.lower() in ['.md', '.qmd']:
            files_to_process = [path]
        else:
            print(f"Error: '{path}' is not a markdown file (.md or .qmd)")
            return 1
    else:
        files_to_process = list(find_markdown_files(path))

    if not files_to_process:
        print("No markdown files found")
        return 0

    print(f"Found {len(files_to_process)} markdown file(s)")

    if args.dry_run:
        print("\nDRY RUN - No files will be modified")

    modified_count = 0

    for file_path in files_to_process:
        if args.dry_run:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    original_content = f.read()
                fixed_content = fix_markdown_lists(original_content)
                if original_content != fixed_content:
                    print(f"Would fix: {file_path}")
                    modified_count += 1
                else:
                    print(f"No changes needed: {file_path}")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
        else:
            if process_file(file_path):
                modified_count += 1

    if args.dry_run:
        print(f"\nDry run complete. {modified_count} file(s) would be modified")
    else:
        print(f"\nProcessing complete. {modified_count} file(s) modified")

    return 0


if __name__ == '__main__':
    exit(main())
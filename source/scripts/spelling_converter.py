#!/usr/bin/env python3
"""
Australian-British Spelling Converter
Intelligently converts American spelling to Australian-British spelling
while preserving code, CSS properties, HTML attributes, and technical terms.
"""

import re
import os
import sys
import csv
import json
from pathlib import Path
from typing import Dict, List, Tuple, Set

class SpellingConverter:
    def __init__(self, mode='hybrid'):
        self.mode = mode

        # Safe explicit mappings (high confidence conversions)
        self.safe_mappings = {
            # -ize to -ise patterns
            r'\borganize\b': 'organise',
            r'\borganized\b': 'organised',
            r'\borganizing\b': 'organising',
            r'\borganization\b': 'organisation',
            r'\borganizations\b': 'organisations',
            r'\breorganize\b': 'reorganise',
            r'\breorganized\b': 'reorganised',
            r'\breorganizing\b': 'reorganising',
            r'\banalyze\b': 'analyse',
            r'\banalyzed\b': 'analysed',
            r'\banalyzing\b': 'analysing',
            r'\banalysis\b': 'analysis',  # Already correct
            r'\brealiz(e|ed|ing|ation)\b': lambda m: m.group(0).replace('realiz', 'realis'),
            r'\bmaterialize\b': 'materialise',
            r'\bmaterialized\b': 'materialised',
            r'\bmaterializing\b': 'materialising',
            r'\bpersonalize\b': 'personalise',
            r'\bpersonalized\b': 'personalised',
            r'\bpersonalizing\b': 'personalising',
            r'\bfinalize\b': 'finalise',
            r'\bfinalized\b': 'finalised',
            r'\bfinalizing\b': 'finalising',
            r'\butilize\b': 'utilise',
            r'\butilized\b': 'utilised',
            r'\butilizing\b': 'utilising',
            r'\butilization\b': 'utilisation',
            r'\bcategorize\b': 'categorise',
            r'\bcategorized\b': 'categorised',
            r'\bcategorizing\b': 'categorising',
            r'\bcentralize\b': 'centralise',
            r'\bcentralized\b': 'centralised',
            r'\bcentralizing\b': 'centralising',
            r'\bminimize\b': 'minimise',
            r'\bminimized\b': 'minimised',
            r'\bminimizing\b': 'minimising',

            # -or to -our patterns
            r'\bcolor\b': 'colour',
            r'\bcolors\b': 'colours',
            r'\bcolored\b': 'coloured',
            r'\bcoloring\b': 'colouring',
            r'\bbehavior\b': 'behaviour',
            r'\bbehaviors\b': 'behaviours',
            r'\bbehavioral\b': 'behavioural',
            r'\bfavor\b': 'favour',
            r'\bfavors\b': 'favours',
            r'\bfavored\b': 'favoured',
            r'\bfavoring\b': 'favouring',
            r'\bhonor\b': 'honour',
            r'\bhonors\b': 'honours',
            r'\bhonored\b': 'honoured',
            r'\bhonoring\b': 'honouring',
            r'\bhumor\b': 'humour',
            r'\bhumors\b': 'humours',
            r'\blabor\b': 'labour',
            r'\blabors\b': 'labours',
            r'\blabored\b': 'laboured',
            r'\blaboring\b': 'labouring',
            r'\bharbor\b': 'harbour',
            r'\bharbors\b': 'harbours',
            r'\bneighbor\b': 'neighbour',
            r'\bneighbors\b': 'neighbours',

            # -er to -re patterns
            r'\bcenter\b': 'centre',
            r'\bcenters\b': 'centres',
            r'\bcentered\b': 'centred',
            r'\bcentering\b': 'centring',
        }

        # Regex patterns for systematic conversion (more restrictive)
        self.pattern_mappings = {
            # -ize/-ise patterns (common roots only)
            r'\b(organ|anal|real|material|personal|final|util|categor|central|minim)ize\b': r'\1ise',
            r'\b(organ|anal|real|material|personal|final|util|categor|central|minim)ized\b': r'\1ised',
            r'\b(organ|anal|real|material|personal|final|util|categor|central|minim)izing\b': r'\1ising',
            r'\b(organ|anal|real|material|personal|final|util|categor|central|minim)ization\b': r'\1isation',
            r'\b(organ)izational\b': r'\1isational',

            # -or/-our patterns (specific words only)
            r'\b(col|behavi|fav|hon|hum|lab|harb|neighb)or\b': r'\1our',
            r'\b(col|behavi|fav|hon|hum|lab|harb|neighb)ors\b': r'\1ours',
            r'\b(col|behavi|fav|hon|hum|lab|harb|neighb)ored\b': r'\1oured',
            r'\b(col|behavi|fav|hon|hum|lab|harb|neighb)oring\b': r'\1ouring',

            # -er/-re patterns (specific words only)
            r'\b(cen)ter\b': r'\1tre',
            r'\b(cen)ters\b': r'\1tres',
            r'\b(cen)tered\b': r'\1tred',
            r'\b(cen)tering\b': r'\1tring',
        }

        # Words to never convert (exceptions)
        self.exceptions = {
            # Common words that shouldn't be converted
            'seize', 'seized', 'seizing', 'seizure',
            'prize', 'prized', 'prizing',
            'size', 'sized', 'sizing',
            'capsize', 'capsized', 'capsizing',
            'maize',
            'froze', 'froze',
            # -or words that shouldn't become -our
            'actor', 'actors', 'doctor', 'doctors', 'editor', 'editors',
            'factor', 'factors', 'sector', 'sectors', 'motor', 'motors',
            'major', 'majors', 'minor', 'minors', 'prior', 'priors',
            'senior', 'seniors', 'junior', 'juniors',
            'professor', 'professors', 'visitor', 'visitors',
            'error', 'errors', 'terror', 'terrors', 'horror', 'horrors',
            # -er words that shouldn't become -re
            'after', 'water', 'paper', 'under', 'over', 'never',
            'other', 'another', 'weather', 'whether', 'letter', 'better',
            'computer', 'computers', 'chapter', 'chapters',
            'number', 'numbers', 'member', 'members',
        }

        # Contexts to preserve (don't change spelling within these)
        self.preserve_contexts = [
            # CSS properties and values
            r'color\s*:\s*[^;]+;',
            r'background-color\s*:\s*[^;]+;',
            r'border-color\s*:\s*[^;]+;',
            r'text-align\s*:\s*center\s*;',
            r'align-items\s*:\s*center\s*;',
            r'justify-content\s*:\s*center\s*;',

            # CSS variable names
            r'--[a-zA-Z-]*color[a-zA-Z-]*',
            r'--[a-zA-Z-]*center[a-zA-Z-]*',

            # HTML attributes
            r'class\s*=\s*["\'][^"\']*["\']',
            r'id\s*=\s*["\'][^"\']*["\']',
            r'style\s*=\s*["\'][^"\']*["\']',

            # URLs and file paths
            r'https?://[^\s<>"]+',
            r'href\s*=\s*["\'][^"\']*["\']',
            r'src\s*=\s*["\'][^"\']*["\']',

            # Code blocks and inline code
            r'```[^`]*```',
            r'`[^`]+`',

            # Quarto/YAML front matter
            r'^---\s*$.*?^---\s*$',

            # HTML/XML tags
            r'<[^>]+>',

            # JavaScript/JSON
            r'\{[^}]*\}',
            r'\[[^\]]*\]',

            # File extensions and technical terms
            r'\.[a-zA-Z0-9]+$',
            r'[A-Z][a-zA-Z]*[A-Z][a-zA-Z]*',  # CamelCase
        ]

        # File extensions to process
        self.target_extensions = {'.md', '.qmd', '.html', '.txt', '.css'}

        # Custom word list (loaded from external files)
        self.custom_mappings = {}

        # Compile regex patterns for efficiency
        self.compiled_preserves = [re.compile(pattern, re.MULTILINE | re.DOTALL)
                                  for pattern in self.preserve_contexts]

    def load_word_list(self, file_path: Path) -> None:
        """Load custom word mappings from a file (CSV, JSON, or text format)."""
        if not file_path.exists():
            print(f"Warning: Word list file {file_path} not found")
            return

        file_ext = file_path.suffix.lower()

        try:
            if file_ext == '.csv':
                self._load_csv(file_path)
            elif file_ext == '.json':
                self._load_json(file_path)
            elif file_ext in ['.txt', '.list']:
                self._load_text(file_path)
            else:
                print(f"Warning: Unsupported word list format: {file_ext}")
                print("Supported formats: .csv, .json, .txt, .list")
        except Exception as e:
            print(f"Error loading word list {file_path}: {e}")

    def _load_csv(self, file_path: Path) -> None:
        """Load CSV format: from,to (with optional header)."""
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)

            # Skip header if it looks like one
            first_row = next(reader, None)
            if first_row and first_row[0].lower() in ['from', 'american', 'original', 'old']:
                pass  # Skip header
            else:
                # Process first row as data
                if first_row and len(first_row) >= 2:
                    self.custom_mappings[rf'\b{re.escape(first_row[0])}\b'] = first_row[1]

            # Process remaining rows
            for row in reader:
                if len(row) >= 2 and row[0].strip() and row[1].strip():
                    american = row[0].strip()
                    british = row[1].strip()
                    self.custom_mappings[rf'\b{re.escape(american)}\b'] = british

    def _load_json(self, file_path: Path) -> None:
        """Load JSON format: {"american": "british", ...}."""
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, dict):
            for american, british in data.items():
                if isinstance(american, str) and isinstance(british, str):
                    self.custom_mappings[rf'\b{re.escape(american)}\b'] = british
        else:
            raise ValueError("JSON file must contain a dictionary of word mappings")

    def _load_text(self, file_path: Path) -> None:
        """Load text format: american=british (one per line)."""
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line or line.startswith('#'):  # Skip empty lines and comments
                    continue

                if '=' in line:
                    american, british = line.split('=', 1)
                    american = american.strip()
                    british = british.strip()
                    if american and british:
                        self.custom_mappings[rf'\b{re.escape(american)}\b'] = british
                else:
                    print(f"Warning: Invalid format on line {line_num}: {line}")
                    print("Expected format: american=british")

    def should_preserve_context(self, text: str, start: int, end: int) -> bool:
        """Check if the match is within a context that should be preserved."""
        for preserve_regex in self.compiled_preserves:
            for match in preserve_regex.finditer(text):
                if match.start() <= start < match.end() or match.start() < end <= match.end():
                    return True
        return False

    def convert_text(self, text: str) -> Tuple[str, List[str]]:
        """Convert American spelling to British spelling in text."""
        changes = []
        result = text

        # Choose mappings based on mode
        if self.mode == 'safe':
            mappings = {**self.safe_mappings, **self.custom_mappings}
        elif self.mode == 'regex':
            mappings = {**self.pattern_mappings, **self.custom_mappings}
        else:  # hybrid mode
            mappings = {**self.safe_mappings, **self.pattern_mappings, **self.custom_mappings}

        for american_pattern, british_replacement in mappings.items():
            pattern = re.compile(american_pattern, re.IGNORECASE)

            # Find all matches first
            matches = list(pattern.finditer(result))

            # Process matches in reverse order to maintain positions
            for match in reversed(matches):
                start, end = match.span()

                # Skip if within preserved context
                if self.should_preserve_context(result, start, end):
                    continue

                original = match.group(0)

                # Skip if word is in exceptions list (for regex patterns)
                if self.mode in ['regex', 'hybrid'] and original.lower() in self.exceptions:
                    continue

                # Handle callable replacements (for complex patterns)
                if callable(british_replacement):
                    replacement = british_replacement(match)
                else:
                    # Handle regex substitution patterns
                    if '\\1' in british_replacement:
                        replacement = re.sub(american_pattern, british_replacement, original, flags=re.IGNORECASE)
                    else:
                        # Preserve original case for explicit mappings
                        if original.isupper():
                            replacement = british_replacement.upper()
                        elif original.istitle():
                            replacement = british_replacement.title()
                        else:
                            replacement = british_replacement

                result = result[:start] + replacement + result[end:]
                changes.append(f"{original} → {replacement}")

        return result, changes

    def process_file(self, file_path: Path, dry_run: bool = False) -> Tuple[bool, List[str]]:
        """Process a single file for spelling conversion."""
        try:
            # Read file with UTF-8 encoding
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()

            # Convert spelling
            converted_content, changes = self.convert_text(original_content)

            # Only write if changes were made and not in dry-run mode
            if changes:
                if not dry_run:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(converted_content)
                return True, changes

            return False, []

        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return False, []

    def process_directory(self, directory: Path, dry_run: bool = False) -> Dict[str, List[str]]:
        """Process all eligible files in directory and subdirectories."""
        all_changes = {}

        for file_path in directory.rglob('*'):
            if file_path.is_file() and file_path.suffix in self.target_extensions:
                changed, file_changes = self.process_file(file_path, dry_run)

                if changed:
                    relative_path = file_path.relative_to(directory)
                    all_changes[str(relative_path)] = file_changes
                    if dry_run:
                        print(f"Would update: {relative_path} ({len(file_changes)} changes)")
                    else:
                        print(f"✓ Updated: {relative_path} ({len(file_changes)} changes)")

        return all_changes

    def generate_report(self, changes: Dict[str, List[str]]) -> str:
        """Generate a summary report of all changes made."""
        if not changes:
            return "No spelling changes needed."

        report = f"Spelling Conversion Report\n{'='*50}\n\n"
        report += f"Files processed: {len(changes)}\n"

        total_changes = sum(len(file_changes) for file_changes in changes.values())
        report += f"Total changes: {total_changes}\n\n"

        for file_path, file_changes in changes.items():
            report += f"{file_path}:\n"
            for change in file_changes[:10]:  # Limit to first 10 changes per file
                report += f"  • {change}\n"
            if len(file_changes) > 10:
                report += f"  ... and {len(file_changes) - 10} more changes\n"
            report += "\n"

        return report

def main():
    """Main function to run the spelling converter."""
    import argparse

    parser = argparse.ArgumentParser(description='Convert American spelling to Australian-British spelling')
    parser.add_argument('path', help='Directory or file path to process')
    parser.add_argument('--mode', choices=['safe', 'regex', 'hybrid'], default='hybrid',
                       help='Conversion mode: safe (explicit mappings only), regex (pattern-based), hybrid (both)')
    parser.add_argument('--wordlist', '-w', type=str,
                       help='Custom word list file (CSV, JSON, or TXT format)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be changed without making modifications')

    args = parser.parse_args()
    path = Path(args.path)

    if not path.exists():
        print(f"Error: {path} does not exist")
        sys.exit(1)

    converter = SpellingConverter(mode=args.mode)

    # Load custom word list if provided
    if args.wordlist:
        wordlist_path = Path(args.wordlist)
        print(f"Loading custom word list: {wordlist_path}")
        converter.load_word_list(wordlist_path)
        custom_count = len(converter.custom_mappings)
        print(f"Loaded {custom_count} custom word mappings")

    if path.is_file():
        # Single file mode
        if args.dry_run:
            print(f"DRY RUN - Analyzing American spelling in: {path}")
        else:
            print(f"Converting American spelling to Australian-British spelling in: {path}")
        print(f"Mode: {args.mode}")
        print("=" * 60)

        changed, file_changes = converter.process_file(path, args.dry_run)

        if changed:
            if args.dry_run:
                print(f"Would update: {path.name} ({len(file_changes)} changes)")
                print("\nChanges that would be made:")
            else:
                print(f"✓ Updated: {path.name} ({len(file_changes)} changes)")
                print("\nChanges made:")
            for change in file_changes:
                print(f"  • {change}")
        else:
            print("No spelling changes needed.")

    elif path.is_dir():
        # Directory mode
        if args.dry_run:
            print(f"DRY RUN - Analyzing American spelling in: {path}")
        else:
            print(f"Converting American spelling to Australian-British spelling in: {path}")
        print(f"Mode: {args.mode}")
        print("=" * 60)

        changes = converter.process_directory(path, args.dry_run)

        print("\n" + "=" * 60)
        report = converter.generate_report(changes)
        if args.dry_run and changes:
            report = report.replace("Spelling Conversion Report", "Spelling Analysis Report (DRY RUN)")
        print(report)

        # Save detailed report only if not dry run
        if not args.dry_run and changes:
            report_file = path / "spelling_conversion_report.txt"
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(converter.generate_report(changes))
            print(f"Detailed report saved to: {report_file}")
        elif args.dry_run and changes:
            print("\nDry run complete. No files were modified.")
    else:
        print(f"Error: {path} is neither a file nor a directory")
        sys.exit(1)

if __name__ == "__main__":
    main()
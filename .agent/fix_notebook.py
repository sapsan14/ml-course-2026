#!/usr/bin/env python3
"""
Fix Jupyter Notebook for Grading Engine Compliance

This script ensures notebooks pass W291 and E303 style checks by:
1. Removing blank lines from all cells
2. Ensuring proper newline formatting
3. Removing trailing whitespace

Usage: python3 fix_notebook.py <notebook.ipynb>
"""

import json
import sys


def fix_notebook_for_grading(filepath):
    """Fix notebook to comply with grading engine requirements."""
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    changes = []
    
    for i, cell in enumerate(nb['cells']):
        source = cell.get('source', [])
        if not source:
            continue
        
        original_len = len(source)
        
        # Step 1: Remove blank lines (just "\n")
        new_source = [line for line in source if line != '\n']
        if len(new_source) != original_len:
            changes.append(f"Cell {i}: Removed {original_len - len(new_source)} blank lines")
        
        # Step 2: Remove trailing whitespace from all lines (except the \n itself)
        for j in range(len(new_source)):
            line = new_source[j]
            if line.endswith('\n'):
                content = line[:-1].rstrip()
                if content + '\n' != line:
                    changes.append(f"Cell {i}, line {j}: Removed trailing whitespace")
                    new_source[j] = content + '\n'
            else:
                content = line.rstrip()
                if content != line:
                    changes.append(f"Cell {i}, line {j}: Removed trailing whitespace")
                    new_source[j] = content
        
        # Step 3: Ensure proper newline formatting
        # - All lines except last must end with \n
        # - Last line must NOT end with \n
        for j in range(len(new_source)):
            if j < len(new_source) - 1:  # Not the last line
                if not new_source[j].endswith('\n'):
                    new_source[j] = new_source[j] + '\n'
                    changes.append(f"Cell {i}, line {j}: Added missing \\n")
            else:  # Last line
                if new_source[j].endswith('\n'):
                    new_source[j] = new_source[j].rstrip('\n')
                    changes.append(f"Cell {i}, line {j}: Removed \\n from last line")
        
        cell['source'] = new_source
    
    # Save the fixed notebook
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2, ensure_ascii=False)
    
    if changes:
        print(f"Fixed {filepath}:")
        for change in changes[:20]:  # Show first 20 changes
            print(f"  - {change}")
        if len(changes) > 20:
            print(f"  ... and {len(changes) - 20} more changes")
    else:
        print(f"✓ {filepath} already compliant")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 fix_notebook.py <notebook.ipynb>")
        sys.exit(1)
    
    fix_notebook_for_grading(sys.argv[1])

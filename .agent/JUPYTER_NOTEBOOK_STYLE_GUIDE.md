# Jupyter Notebook Style Guide for Grading Engine

## CRITICAL: Grading Engine Behavior

The grading engine converts Jupyter notebooks to Python files using a process similar to `jupyter nbconvert --to script`. This conversion has specific requirements that MUST be followed to avoid W291 (trailing whitespace) and E303 (too many blank lines) errors.

## Required Notebook Structure

### 1. NO Blank Lines in Cells

**NEVER** include blank lines (just `"\n"`) in any cell source:

```python
# ❌ WRONG - will cause W291 errors
{
  "source": [
    "import pandas as pd\n",
    "\n",  # <- This blank line causes W291!
    "df = pd.read_csv('data.csv')\n"
  ]
}

# ✓ CORRECT
{
  "source": [
    "import pandas as pd\n",
    "df = pd.read_csv('data.csv')\n"
  ]
}
```

### 2. Last Line of Each Cell Must NOT End with `\n`

**The last line of every cell must NOT have a trailing newline:**

```python
# ❌ WRONG
{
  "source": [
    "import pandas as pd\n",
    "import numpy as np\n"  # <- Last line should NOT end with \n
  ]
}

# ✓ CORRECT
{
  "source": [
    "import pandas as pd\n",
    "import numpy as np"  # <- No \n at the end
  ]
}
```

### 3. All Other Lines MUST End with `\n`

**Every line except the last one must end with `\n`:**

```python
# ✓ CORRECT
{
  "source": [
    "import pandas as pd\n",  # <- Has \n
    "import numpy as np\n",   # <- Has \n
    "import matplotlib.pyplot as plt"  # <- Last line, no \n
  ]
}
```

## Automated Fix Script

Use this script to fix any notebook:

```python
#!/usr/bin/env python3
import json

def fix_notebook_for_grading(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    for i, cell in enumerate(nb['cells']):
        source = cell.get('source', [])
        if not source:
            continue
        
        # Step 1: Remove any blank lines (just "\n")
        new_source = [line for line in source if line != '\n']
        
        # Step 2: Ensure all lines except last end with \n
        for j in range(len(new_source)):
            if j < len(new_source) - 1:  # Not the last line
                if not new_source[j].endswith('\n'):
                    new_source[j] = new_source[j] + '\n'
            else:  # Last line
                if new_source[j].endswith('\n'):
                    new_source[j] = new_source[j].rstrip('\n')
        
        cell['source'] = new_source
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Fixed {filepath}")

if __name__ == '__main__':
    import sys
    fix_notebook_for_grading(sys.argv[1])
```

## Common Errors and Solutions

### W291: trailing whitespace

**Cause:** Blank lines in cells or lines with only whitespace

**Solution:**
1. Remove all lines that are just `"\n"` from cell source
2. Remove trailing spaces from all lines: `line.rstrip() + '\n'`

### E303: too many blank lines

**Cause:** Multiple consecutive blank lines (usually from adding separators between cells)

**Solution:**
1. Do NOT add blank lines between cells
2. The grading engine handles cell separation automatically

## Verification

After fixing, verify the notebook:

```python
import json

with open('notebook.ipynb') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    source = cell.get('source', [])
    
    # Check for blank lines
    for j, line in enumerate(source):
        if line == '\n':
            print(f"❌ Cell {i}, line {j}: Blank line found!")
        
        # Check last line doesn't end with \n
        if j == len(source) - 1 and line.endswith('\n'):
            print(f"❌ Cell {i}: Last line ends with \\n!")
        
        # Check non-last lines end with \n
        if j < len(source) - 1 and not line.endswith('\n'):
            print(f"❌ Cell {i}, line {j}: Missing \\n!")
```

## Summary Checklist

Before submitting a notebook to the grading engine:

- [ ] No blank lines (`"\n"`) in any cell
- [ ] No trailing whitespace on any line (except the `\n` itself)
- [ ] All lines except the last one in each cell end with `\n`
- [ ] The last line in each cell does NOT end with `\n`
- [ ] No markdown cells with only `"\n"` content
- [ ] Run the fix script above to ensure compliance

## Why This Matters

The grading engine converts notebooks like this:

```
Cell 1 (code):   "import pandas\n"
                 "import numpy"
                 
Cell 2 (markdown): "# Title"

Cell 3 (code):   "df = pd.read_csv('data.csv')"
```

Becomes:

```python
import pandas
import numpy
# Title
df = pd.read_csv('data.csv')
```

If cells have trailing `\n`, the conversion creates blank lines that trigger W291 errors.

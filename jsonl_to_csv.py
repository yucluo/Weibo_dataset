#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 09:13:11 2025

@author: yuchenluo
"""

import json
import pandas as pd
from pathlib import Path

# 1. Path to your folder containing JSONL files
data_folder = Path("raw_data")

# 2. Collect all .jsonl files
jsonl_files = list(data_folder.glob("*.jsonl"))
print(f"Found {len(jsonl_files)} JSONL files.")

# 3. Read and flatten each JSON object
records = []
for file in jsonl_files:
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                records.append(data)
            except json.JSONDecodeError:
                print(f"Skipping bad line in {file}")

# 4. Convert to DataFrame (keys become columns)
df = pd.json_normalize(records)   # flattens nested JSONs automatically

# 5. Save as a CSV
df.to_csv("cleaned_data.csv", index=False)

print(f"✅ Saved {len(df)} rows to cleaned_data.csv")

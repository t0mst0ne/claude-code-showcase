---
description: Analyzes CSV files, generates summary stats, and plots quick visualizations using Python and pandas.
---

# CSV Data Summarizer

This workflow analyzes CSV files and provides comprehensive summaries with statistical insights and visualizations.

## When to Use

Use this workflow whenever you:
- Upload or reference a CSV file
- Need to summarize, analyze, or visualize tabular data
- Need insights from CSV data
- Want to understand data structure and quality

## Instructions

1.  **Analyze the Data**:
    -   Load the CSV file using pandas.
    -   Identify data structure (column types, date columns, numeric columns).
    -   Generate summary statistics.
    -   Check for missing values.

2.  **Generate Visualizations**:
    -   Create visualizations based on the data type (e.g., time-series plots for dates, correlation heatmaps for numerics, distributions).
    -   Use `matplotlib` and `seaborn` for plotting.

3.  **Present Results**:
    -   Provide a comprehensive text summary.
    -   Display the generated visualizations.

## Script Usage

The original skill uses a python script `analyze.py`. You can run a similar analysis using the following steps in a python script:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_csv(file_path):
    df = pd.read_csv(file_path)
    print("Dataset Overview:")
    print(df.info())
    print("\nSummary Statistics:")
    print(df.describe())
    # Add custom visualization logic here based on columns
```

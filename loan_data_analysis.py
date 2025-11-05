#!/usr/bin/env python3
"""
Loan Data Analysis

This script analyzes loan data from 2007 using pandas with memory optimization techniques.
It processes the data in chunks to handle large datasets efficiently and performs
data type optimization to reduce memory usage.
"""

import pandas as pd
import numpy as np

# Set pandas display options
pd.options.display.max_columns = 99


def explore_data_sample():
    """Load and display first 5 rows of the dataset."""
    print("Loading first 5 rows of the dataset...")
    first_five = pd.read_csv('loans_2007.csv', nrows=5)
    print(first_five)
    return first_five


def calculate_memory_usage():
    """Calculate memory usage for different chunk sizes."""
    print("\nCalculating memory usage for 1000 rows...")
    thousand_chunk = pd.read_csv('loans_2007.csv', nrows=1000)
    memory_mb = thousand_chunk.memory_usage(deep=True).sum() / (1024 * 1024)
    print(f"Memory usage for 1000 rows: {memory_mb:.2f} MB")
    
    print("\nCalculating memory usage for 3000-row chunks...")
    chunk_iter = pd.read_csv('loans_2007.csv', chunksize=3000)
    for i, chunk in enumerate(chunk_iter):
        memory_mb = chunk.memory_usage(deep=True).sum() / (1024 * 1024)
        print(f"Chunk {i+1}: {memory_mb:.2f} MB")


def count_total_rows():
    """Count total number of rows in the dataset."""
    print("\nCounting total rows in dataset...")
    chunk_iter = pd.read_csv('loans_2007.csv', chunksize=3000)
    total_rows = 0
    for chunk in chunk_iter:
        total_rows += len(chunk)
    print(f"Total rows: {total_rows}")
    return total_rows


def analyze_column_types():
    """Analyze numeric vs string column types across chunks."""
    print("\nAnalyzing column types across chunks...")
    loans_chunks = pd.read_csv('loans_2007.csv', chunksize=3000)
    
    numeric = []
    string = []
    for lc in loans_chunks:
        nums = lc.select_dtypes(include=[np.number]).shape[1]
        numeric.append(nums)
        strs = lc.select_dtypes(include=['object']).shape[1]
        string.append(strs)
    
    print(f"Numeric columns per chunk: {numeric}")
    print(f"String columns per chunk: {string}")
    
    return numeric, string


def check_string_column_consistency():
    """Check if string columns are consistent across chunks."""
    print("\nChecking string column consistency...")
    obj_cols = []
    chunk_iter = pd.read_csv('loans_2007.csv', chunksize=3000)
    
    for chunk in chunk_iter:
        chunk_obj_cols = chunk.select_dtypes(include=['object']).columns.tolist()
        if len(obj_cols) > 0:
            is_same = obj_cols == chunk_obj_cols
            if not is_same:
                print("Inconsistency found:")
                print("Overall obj cols:", obj_cols)
                print("Chunk obj cols:", chunk_obj_cols)
        else:
            obj_cols = chunk_obj_cols
    
    return obj_cols


def analyze_unique_values():
    """Analyze unique values in string columns."""
    print("\nAnalyzing unique values in string columns...")
    loans_chunks = pd.read_csv('loans_2007.csv', chunksize=3000)
    
    uniques = {}
    for lc in loans_chunks:
        strings_only = lc.select_dtypes(include=['object'])
        cols = strings_only.columns
        for c in cols:
            val_counts = strings_only[c].value_counts()
            if c in uniques:
                uniques[c].append(val_counts)
            else:
                uniques[c] = [val_counts]
    
    uniques_combined = {}
    for col in uniques:
        u_concat = pd.concat(uniques[col])
        u_group = u_concat.groupby(u_concat.index).sum()
        uniques_combined[col] = u_group
        if u_group.shape[0] < 50:
            print(f"{col}: {u_group.shape[0]} unique values")
    
    return uniques_combined


def analyze_missing_values():
    """Analyze missing values in float columns."""
    print("\nAnalyzing missing values in float columns...")
    loans_chunks = pd.read_csv('loans_2007.csv', chunksize=3000)
    
    missing = []
    for lc in loans_chunks:
        floats = lc.select_dtypes(include=['float'])
        missing.append(floats.apply(pd.isnull).sum())
    
    combined_missing = pd.concat(missing)
    missing_summary = combined_missing.groupby(combined_missing.index).sum().sort_values()
    print("Missing values by column:")
    print(missing_summary)
    
    return missing_summary


def calculate_total_memory():
    """Calculate total memory usage across all chunks."""
    print("\nCalculating total memory usage...")
    loans_chunks = pd.read_csv('loans_2007.csv', chunksize=3000)
    
    mem_usage = []
    for lc in loans_chunks:
        mem_usage.append(lc.memory_usage(deep=True).sum() / 1024 ** 2)
    
    total_memory = sum(mem_usage)
    print(f"Total memory usage: {total_memory:.2f} MB")
    
    return total_memory


def create_value_counts_dict():
    """Create dictionary of value counts for string columns."""
    print("\nCreating value counts dictionary...")
    chunk_iter = pd.read_csv('loans_2007.csv', chunksize=3000)
    str_cols_vc = {}
    
    for chunk in chunk_iter:
        str_cols = chunk.select_dtypes(include=['object'])
        for col in str_cols.columns:
            current_col_vc = str_cols[col].value_counts()
            if col in str_cols_vc:
                str_cols_vc[col].append(current_col_vc)
            else:
                str_cols_vc[col] = [current_col_vc]
    
    # Combine the value counts
    combined_vcs = {}
    for col in str_cols_vc:
        combined_vc = pd.concat(str_cols_vc[col])
        final_vc = combined_vc.groupby(combined_vc.index).sum()
        combined_vcs[col] = final_vc
    
    return combined_vcs


def display_useful_columns_info(combined_vcs):
    """Display information for useful object columns."""
    useful_obj_cols = [
        'term', 'sub_grade', 'emp_title', 'home_ownership', 
        'verification_status', 'issue_d', 'purpose', 'earliest_cr_line', 
        'revol_util', 'last_pymnt_d', 'last_credit_pull_d'
    ]
    
    print("\nValue counts for useful columns:")
    for col in useful_obj_cols:
        if col in combined_vcs:
            print(f"\n{col}:")
            print(combined_vcs[col])
            print("-" * 50)


def optimize_data_types():
    """Optimize data types for memory efficiency."""
    print("\nOptimizing data types...")
    
    # Define data type conversions
    convert_col_dtypes = {
        "sub_grade": "category", 
        "home_ownership": "category", 
        "verification_status": "category", 
        "purpose": "category"
    }
    
    # Process data with optimized types
    chunk_iter = pd.read_csv(
        'loans_2007.csv', 
        chunksize=3000, 
        dtype=convert_col_dtypes, 
        parse_dates=["issue_d", "earliest_cr_line", "last_pymnt_d", "last_credit_pull_d"]
    )
    
    # Clean and convert specific columns
    for chunk in chunk_iter:
        # Clean term column (remove " months" suffix)
        term_cleaned = chunk['term'].str.lstrip(" ").str.rstrip(" months")
        chunk['term'] = pd.to_numeric(term_cleaned)
        
        # Clean revol_util column (remove "%" suffix)
        revol_cleaned = chunk['revol_util'].str.rstrip("%")
        chunk['revol_util'] = pd.to_numeric(revol_cleaned)
        
        # Drop rows that are completely empty
        chunk = chunk.dropna(how='all')
    
    print("Data types optimized successfully!")
    print("Sample data types after optimization:")
    print(chunk.dtypes)
    
    return chunk


def analyze_missing_values_optimized():
    """Analyze missing values after optimization."""
    print("\nAnalyzing missing values after optimization...")
    
    convert_col_dtypes = {
        "sub_grade": "category", 
        "home_ownership": "category", 
        "verification_status": "category", 
        "purpose": "category"
    }
    
    chunk_iter = pd.read_csv(
        'loans_2007.csv', 
        chunksize=3000, 
        dtype=convert_col_dtypes, 
        parse_dates=["issue_d", "earliest_cr_line", "last_pymnt_d", "last_credit_pull_d"]
    )
    
    mv_counts = {}
    for chunk in chunk_iter:
        # Clean columns
        term_cleaned = chunk['term'].str.lstrip(" ").str.rstrip(" months")
        revol_cleaned = chunk['revol_util'].str.rstrip("%")
        chunk['term'] = pd.to_numeric(term_cleaned)
        chunk['revol_util'] = pd.to_numeric(revol_cleaned)
        chunk = chunk.dropna(how='all')
        
        # Count missing values in float columns
        float_cols = chunk.select_dtypes(include=['float'])
        for col in float_cols.columns:
            missing_values = len(chunk) - chunk[col].count()
            if col in mv_counts:
                mv_counts[col] = mv_counts[col] + missing_values
            else:
                mv_counts[col] = missing_values
    
    print("Missing values after optimization:")
    for col, count in sorted(mv_counts.items(), key=lambda x: x[1]):
        print(f"{col}: {count}")
    
    return mv_counts


def main():
    """Main function to run the complete analysis."""
    print("=" * 60)
    print("LOAN DATA ANALYSIS - MISSION 165 SOLUTIONS")
    print("=" * 60)
    
    # Basic exploration
    explore_data_sample()
    calculate_memory_usage()
    count_total_rows()
    
    # Column analysis
    analyze_column_types()
    obj_cols = check_string_column_consistency()
    
    # Unique values and missing data analysis
    combined_vcs = analyze_unique_values()
    analyze_missing_values()
    calculate_total_memory()
    
    # Detailed analysis of useful columns
    display_useful_columns_info(combined_vcs)
    
    # Data optimization
    optimize_data_types()
    analyze_missing_values_optimized()
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
# Loan Data Analysis 

A comprehensive data analysis project that processes and analyzes loan data from 2007 using memory-efficient techniques in Python with pandas.

## Overview

This project demonstrates advanced data processing techniques for handling large datasets efficiently. It analyzes loan data using chunked processing to optimize memory usage and performs data type optimization to reduce the overall memory footprint.

## Features

- **Memory-Efficient Processing**: Uses pandas chunking to process large datasets without loading everything into memory
- **Data Type Optimization**: Converts string columns to categories and optimizes numeric types
- **Comprehensive Analysis**: Provides detailed insights into data structure, missing values, and column characteristics
- **Data Cleaning**: Handles string formatting issues and converts data to appropriate types

## Dataset

The analysis uses `loans_2007.csv`, which contains loan data with the following characteristics:
- **Total Records**: 42,538 loans
- **Columns**: 52 features including loan amounts, interest rates, borrower information, and loan status
- **Size**: Approximately 66MB when fully loaded

## Key Analysis Components

### 1. Data Exploration
- Sample data inspection
- Memory usage calculation across different chunk sizes
- Column type analysis (numeric vs string)

### 2. Data Quality Assessment
- Missing value analysis across all columns
- String column consistency checks
- Unique value counts for categorical data

### 3. Data Optimization
- Conversion of appropriate string columns to category type
- Date parsing for temporal columns
- Numeric conversion with data cleaning

### 4. Memory Optimization Results
- **Before optimization**: ~66MB total memory usage
- **After optimization**: Significant reduction through categorical encoding and proper data types

## Installation

1. Clone this repository:
```bash
git clone https://github.com/ElijahMugariri99/loan-data-analysis.git
cd loan-data-analysis
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Download the dataset:
   - Get `loans_2007.csv` from [Kaggle Lending Club Dataset](https://www.kaggle.com/datasets/wendykan/lending-club-loan-data)
   - Place it in the project root directory

## Usage

### Quick Start
Run the analysis using the provided script:
```bash
./run_analysis.sh
```

### Manual Execution
Run the complete analysis directly:
```bash
python loan_data_analysis.py
```

### Installation as Package
Install the project as a Python package:
```bash
pip install -e .
loan-analysis
```

The script will output:
- Data exploration results
- Memory usage statistics
- Column analysis summaries
- Missing value reports
- Optimization results

## Key Findings

### Column Types
- **31 numeric columns**: Various loan metrics and financial data
- **21 string columns**: Categorical data and text fields

### Data Quality
- Most columns have minimal missing values (< 50 missing entries)
- Some columns like `pub_rec_bankruptcies` have more significant missing data (1,368 entries)

### Optimization Opportunities
- **Categorical columns**: `sub_grade`, `home_ownership`, `verification_status`, `purpose`
- **Date columns**: `issue_d`, `earliest_cr_line`, `last_pymnt_d`, `last_credit_pull_d`
- **Numeric cleaning**: `term` (remove "months"), `revol_util` (remove "%")

## Technical Implementation

### Memory Management
- Uses `chunksize=3000` for processing large datasets
- Implements `dropna(how='all')` to remove completely empty rows
- Monitors memory usage throughout the process

### Data Type Conversions
```python
convert_col_dtypes = {
    "sub_grade": "category", 
    "home_ownership": "category", 
    "verification_status": "category", 
    "purpose": "category"
}
```

### String Cleaning
- Term column: Removes " months" suffix and converts to numeric
- Revolving utilization: Removes "%" suffix and converts to numeric
- Date columns: Parsed using pandas `parse_dates` parameter

## Project Structure

```
loan-data-analysis/
├── loan_data_analysis.py    # Main analysis script 
├── loans_2007.csv          # Dataset (not included in repo)
├── README.md               # This file
├── requirements.txt        # Python dependencies
├── setup.py                # Package setup configuration
├── run_analysis.sh         # Bash script to run analysis
├── .gitignore              # Git ignore rules
└── .git/                   # Git repository data
```

## Requirements

- Python 3.6+
- pandas >= 1.0.0
- numpy >= 1.18.0

## GitHub Setup

This project is ready for GitHub! To push to your GitHub repository:

1. Create a new repository on GitHub (don't initialize with README)
2. Add your GitHub repository as remote:
```bash
git remote add origin https://github.com/ElijahMugariri99/loan-data-analysis.git
```
3. Push to GitHub:
```bash
git push -u origin main
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-analysis`)
3. Commit your changes (`git commit -am 'Add new analysis feature'`)
4. Push to the branch (`git push origin feature/new-analysis`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Original dataset from lending club loan data
- Inspired by Dataquest.ios data analysis challenges
- Built using pandas and numpy for efficient data processing
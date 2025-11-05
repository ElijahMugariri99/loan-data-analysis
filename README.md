<div align="center">

# 📊 Loan Data Analysis

*A comprehensive data analysis project for processing and analyzing loan data with memory-efficient techniques*

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/ElijahMugariri99/loan-data-analysis.git?color=green)](LICENSE)
[![Pandas](https://img.shields.io/badge/Pandas-1.0+-orange.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.18+-red.svg)](https://numpy.org/)

</div>

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
    - [Project Index](#project-index)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## 🎯 Overview

This project provides a comprehensive analysis of loan data from 2007, implementing memory-efficient data processing techniques using pandas and numpy. The analysis focuses on handling large datasets through chunked processing, data type optimization, and thorough exploratory data analysis.


---

## ✨ Features

- **Memory-Efficient Processing**: Handles large datasets using chunked data processing
- **Data Type Optimization**: Converts data types to reduce memory usage by up to 50%
- **Comprehensive Analysis**: 
  - Missing value analysis
  - Column type analysis
  - Unique value exploration
  - Memory usage tracking
- **Date Parsing**: Intelligent parsing of date columns
- **Data Cleaning**: Automated cleaning of percentage and term columns
- **Categorical Optimization**: Converts appropriate columns to category dtype for memory efficiency

---

## 📁 Project Structure

```
loan-data-analysis/
├── 📄 LICENSE                    # MIT License
├── 📖 README.md                  # Project documentation
├── 🐍 loan_data_analysis.py      # Main analysis script
├── 📋 requirements.txt           # Python dependencies
└── ⚙️ setup.py                   # Package setup configuration
```

### Key Components

| File | Purpose |
|------|---------|
| `loan_data_analysis.py` | Main analysis script with memory-efficient data processing |
| `requirements.txt` | Python dependencies (pandas, numpy) |
| `setup.py` | Package configuration and installation setup |

---

## Getting Started

### 📋 Prerequisites

- **Python 3.6+** - Programming language
- **pip** - Package manager

Download the dataset: - Get `loans_2007.csv` from [Kaggle Lending Club Dataset](https://www.kaggle.com/datasets/wendykan/lending-club-loan-data)
- Place it in the project root directory - `loans_2007.csv` (loan data from 2007)

**Required Python packages:**
- `pandas >= 1.0.0` - Data manipulation and analysis
- `numpy >= 1.18.0` - Numerical computing

### 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ElijahMugariri99/loan-data-analysis.git
   cd loan-data-analysis
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Or install as a package:**
   ```bash
   pip install -e .
   ```

### 🚀 Usage

**Prerequisites:** Ensure you have a CSV file named `loans_2007.csv` in your project directory.

**Run the complete analysis:**
```bash
python loan_data_analysis.py
```

**Or use as a package:**
```bash
loan-analysis
```

### 📊 What the Analysis Does

The script performs the following operations:

1. **Data Exploration**: Loads and displays sample data
2. **Memory Analysis**: Calculates memory usage for different chunk sizes
3. **Column Analysis**: Identifies numeric vs string columns
4. **Missing Value Analysis**: Identifies and quantifies missing data
5. **Data Type Optimization**: Converts columns to more efficient data types
6. **Data Cleaning**: Cleans percentage and term columns
7. **Final Report**: Provides comprehensive analysis results

### 💡 Key Functions

- `explore_data_sample()` - Quick data preview
- `calculate_memory_usage()` - Memory usage analysis
- `optimize_data_types()` - Data type optimization for memory efficiency
- `analyze_missing_values()` - Missing data analysis

### ⚡ Performance Features

- **Chunked Processing**: Processes large datasets in 3000-row chunks to manage memory usage
- **Memory Optimization**: Reduces memory usage by converting string columns to categories
- **Efficient Data Types**: Automatically optimizes numeric and date columns
- **Progress Tracking**: Real-time memory usage and processing statistics

**Typical Performance:**
- Memory usage reduction: ~40-60%
- Processing speed: 3000 rows/chunk
- Supports datasets with millions of rows

---

## 🛣️ Roadmap

- [x] **Memory-Efficient Processing**: Implement chunked data processing
- [x] **Data Type Optimization**: Convert columns to optimal data types
- [x] **Missing Value Analysis**: Comprehensive missing data analysis
- [x] **Date Parsing**: Intelligent date column handling
- [ ] **Visualization Module**: Add data visualization capabilities
- [ ] **Statistical Analysis**: Implement advanced statistical methods
- [ ] **Export Functionality**: Add data export options
- [ ] **Configuration File**: Add YAML/JSON configuration support

---

## Contributing

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/ElijahMugariri99/loan-data-analysis.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Dataquest.io** - Project development and analysis methodology
- **Pandas Development Team** - For the excellent data manipulation library
- **NumPy Community** - For numerical computing capabilities
- **Open Source Community** - For continuous inspiration and support

<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---

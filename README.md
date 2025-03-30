# Credit Rating System

## Overview

A credit rating agency that assesses the creditworthiness of financial products, specifically residential mortgage-backed securities (RMBS). Our ratings are critical for investors and institutions in determining the quality and risk associated with mortgage-backed securities.

## Features

- Calculates LTV and DTI ratios.
- Assigns risk scores based on financial parameters.
- Computes the overall credit rating for multiple mortgage applications.
- Supports input from JSON, CSV, and Excel files.
- Includes unit tests to validate calculations and file processing.

## Installation

### Prerequisites

- Python 3.x
- Required dependencies listed in `requirements.txt`

### Setup

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd credit-rating-system
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```


### Running the Tests

For test cases:

```sh
python -m unittest test_credit_rating.py
```

### Processing Data

To calculate credit score, run:

```sh
python credit_rating.py 
```

Supported file formats: `.json`, `.csv`, `.xlsx`

## Technical Decisions & Design

- **LTV and DTI Calculation**: Financial ratios are used to assess the risk level of mortgage applications.
- **Risk Scoring**: Risk evaluation assigns scores based on creditworthiness.
- **File Handling**: It supports multiple formats using `pandas`.
- **Testing**: `unittest` framework for testing of calculations.

## Sample Dataset

A sample dataset with 120 mortgage applications is included in `large_sample.csv` for performance testing.

## Contributors

- Lucky Pathak


# ETL Pipeline Project
27.1.2025

This project implements an ETL (Extract, Transform, Load) pipeline. The pipeline is designed to extract SPY ETF pricing data from Yahoo Finance's API, transform it into a desired format, and load it into a SQLite database for further analysis or storage.

## Project Structure

```
etl_pipeline_project
├── database
│   └── 'created database'
├── src
│   ├── etl_pipeline.py
├── requirements.txt
└── README.md
```

## Overview

The ETL pipeline consists of the following main components:

1. **Extraction**: The process of retrieving data from various sources, such as APIs, databases, or files.
2. **Transformation**: The process of cleaning and formatting the extracted data to meet the requirements of the destination.
3. **Loading**: The process of saving the transformed data into a target system, such as a database or a file.

## Setup

To set up the project, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies listed in `requirements.txt` using pip:

   ```
   pip install -r requirements.txt
   ```

## Running the ETL Pipeline

To run the ETL pipeline, execute the following command in your terminal:

```
python src/etl_pipeline.py
```

Make sure to configure the source and destination settings in the `etl_pipeline.py` file according to your requirements.

## Additional Features

- **Worst Days Analysis**: A script to query the database and find the ETF's worst days from the 2000s.
   - to run: python src/worst_days.py

This project demonstrates practical skills in data extraction, transformation, and loading processes using Python and SQLite.


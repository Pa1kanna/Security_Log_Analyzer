# Security Log Analyzer & Extractor 📊

An automated Python tool designed to streamline SOC workflows by parsing raw server logs for indicators of compromise (IOCs). This script specifically hunts for failed SSH login attempts, isolating the targeted usernames and attacking IP addresses.

## Objective
To demonstrate proficiency in scripting for security automation, utilizing Regular Expressions (Regex) for data extraction, and preparing raw log data for further ingestion into business intelligence and data analytics tools. 

## Features
* **Regex Integration:** Utilizes the `re` library to accurately identify and extract specific data strings from noisy log files.
* **Automated Data Structuring:** Converts unstructured text logs into structured datasets.
* **CSV Export:** Automatically generates a `failed_logins.csv` file, making the threat data immediately ready for visualization in tools like Tableau, Power BI, or Advanced Excel.

## Usage
Ensure that your target log file is named `server.log` and is placed in the same directory as the script.

```bash
# Run the analyzer
python3 log_parser.py


## Expected Output:
The script will output the number of discovered threats to the console and generate a failed_logins.csv file containing the extracted IP addresses and usernames.

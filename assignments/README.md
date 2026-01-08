# Programming for Data Analytics: Assignments

Author: Céaman Collins

## Overview

This folder contains the assignments for the *Programming for Data Analytics (PFDA)* module at ATU. The assignments demonstrate skills in Python programming, data analysis, and visualization across various datasets.

## Setup and Installation

To run the code provided in these assignments:
1. Make sure you have Python installed (version 3.6 or higher is recommended).

### Using `pip`:
Install all required dependencies via the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Using `conda`:
Alternatively, create a Conda environment and install the required dependencies:

```bash
conda create --name <environment-name> --file requirements.txt
```

You can execute these assignments in CodeSpaces, Jupyter Notebook, or by cloning the repository and running the code locally in VSCode.

---

## Technologies Used

The following technologies and tools were used in the assignments:
- **Python**: Core language used for data analysis and scripting.
- **Jupyter Notebook**: Interactive environment for developing and sharing code notebooks.
- **Pandas**: Library for data manipulation and analysis.
- **NumPy**: Library for numerical computations.
- **Matplotlib**: Data visualization library for creating static, animated, and interactive plots.
- **Seaborn**: Statistical data visualization library built on Matplotlib.
- **Requests**: HTTP library for fetching data from APIs and URLs.
- **GitHub**: For version control and automating workflows.

---

## Assignments

### Assignment 2: Northern Bank Holidays

In this assignment, the goal was to create a script that prints out the dates of bank holidays in Northern Ireland by reading data from a JSON file on the UK government website. Additionally, the program should identify the bank holidays that are unique to Northern Ireland (i.e., not occurring in other parts of the UK).

- **Script Name:** [`assignment02-bankholdiays.py`](./assignment2/assignment02-bankholdiays.py)
- **Tasks:**
  1. Print the dates of all bank holidays in Northern Ireland.
  2. (Advanced) Identify and print bank holidays unique to Northern Ireland, using either the name or date of the holidays.

---

### Assignment 3: Domains

The aim of this assignment was to create a pie chart visualizing the distribution of email domains from a dataset of 1,000 people.

- **Notebook Name:** [`assignment03-pie.ipynb`](./assignment3/assignment03-pie.ipynb)
- **Dataset URL:** [Google Drive Link](https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download)
- **Tasks:**
  - Create a pie chart of the email domains in the dataset.
  - Ensure the pie chart is well-designed and visually appealing.

---

### Assignment 5: Population Distribution

This assignment required the analysis of population data from the Central Statistics Office of Ireland. The data highlights differences between male and female populations by age, with additional stratifications and regional analyses.

- **Notebook Name:** [`assignment05-population.ipynb`](./assignment5/assignment05-population.ipynb)
- **Tasks:**
  - **Part 1 (70%):**
    - Analyze the differences between the sexes by age (weighted mean age, population differences). Regional data is not required here.
  - **Part 2 (20%):**
    - Create a variable for a specific age (e.g., 35), group people within five years of that age, and calculate population differences.
  - **Part 3 (10%):**
    - Determine which region in Ireland has the largest population difference between sexes for the specified age group.

---

### Assignment 6: Knock Airport Weather

In this assignment, data from the Knock Airport weather station was analyzed to create plots of various weather metrics.

- **Notebook Name:** [`assignment_6_Weather.ipynb`](./assignment6/assignment_6_Weather.ipynb)
- **Dataset URL:** [Climate Data CSV](https://cli.fusio.net/cli/climate_data/webdata/hly4935.csv)
- **Tasks:**
  - Plot the following:
    - Temperature
    - Mean temperature per day
    - Mean temperature per month (60% of total marks)
  - Additional:
    - Windspeed (accounting for missing data)
    - Rolling windspeed (24-hour averages)
    - Maximum daily windspeed
    - Monthly mean of daily maximum windspeeds (40% of total marks)

---

## Contact

For any questions or further information, please reach out to **Céaman Collins** via GitHub.

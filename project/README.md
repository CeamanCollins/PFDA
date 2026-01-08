# PFDA Project

## Overview

This folder contains the project for the *Programming for Data Analytics (PFDA)* module at ATU. The project focuses on exploring wind speed data, analyzing patterns, and evaluating the feasibility of wind power generation at various locations in Ireland.

## Project Description

The project involves an in-depth analysis of wind speed recordings from Mace Head Atmospheric Research Station and other stations across Ireland. Key objectives include:
- Investigating the station's ability to capture data during significant weather events.
- Assessing wind turbines' operational capacity based on location-specific wind conditions.
- Mapping, ranking, and rating various weather stations around Ireland for wind power generation.
- Modeling and predicting wind speeds using ARIMA techniques for optimized planning.

### Summary of Project

This project has been an exploration in the analyses of wind speed recordings from Mace Head Atmospheric Research Station and other stations around Ireland. 

**Key Findings**:

1. **Investigating Storms**: In this section we looked at 6 major weather events and how they were recorded at Mace Head. This demonstrates the station's ability to capture useful data.

2. **Wind Turbines**: In this section we look at the capabilities of wind turbines to operate in different wind speeds and calculate what proportion of the time a wind turbine would be operational at this location. A turbine at this location would be active around 90% of the time, in-line with and potentially above the typical 85% expected of a normal turbine confirming that this location would be suitable for wind power generation.

3. **National Ratings**: In this section we go about mapping the weather stations around Ireland and rate each location's viability for wind power production. Mace Head ranked second in the national rankings making it an excellent option for a wind farm.

4. **Power Generation**: In this section we look at the theoretical output of a wind turbine and estimate the power generation of a turbine at this location considering specific technical limitations. After creating a function to calculate potential power outputs, we find that a wind turbine would have produced over 200MWh in January 2025 alone.

5. **Monthly Wind Speeds**: In this section we look at average wind speeds by month and look to plot the data in order to identify seasonal trends. By plotting the data in various ways we have identified definite seasonal peaks and troughs, i.e. lower wind speeds in the summer compared to the winter.

6. **Machine Learning**: In this section we go about creating an ARIMA model that could predict what wind speeds could be expected for a particular time period given historical data. Using our function from a previous section and the predicted average wind speeds, we find that out predictions and historical data only differ by around 3%. 

7. **Weather Forecasts**: In this section we get weather forecast data from an API and use it to make predictions about wind power production for the coming week. The values produced are quite different to the expected values from the model produced in the previous section, but it is difficult to say which is a better predictor for the future as that is only known with hindsight.

**Conclusion:** Mace Head's capacity for recording weather data is extensive and detailed. The data has allowed analysis that has put Mace Head in the running as a candidate for a wind farm. The ARIMA model captures seasonal changes incredibly well and has proven to be an accurate predictor of potential power generation for the location. It is yet to be seen how well the model predicts future values, but based on historical data, it is a reliable source for any future planning that might occur at this location.

## Technologies Used

The following technologies and tools were used in the project:
- **Python**: Core language used for data analysis and modeling.
- **Jupyter Notebook**: Interactive environment for developing and sharing code and analysis.
- **Pandas**: Library for data manipulation and analysis.
- **NumPy**: Library for numerical computations.
- **Matplotlib**: Data visualization library for creating static and interactive plots.
- **Seaborn**: Statistical data visualization library built on Matplotlib.
- **ARIMA (via `statsmodels`)**: Model for time series forecasting and analysis.
- **Requests**: HTTP library for fetching data from weather forecast APIs.
- **GitHub**: Version control for managing project history and collaboration.

## Setup and Installation

To execute the code in the project:
1. Clone the repository and navigate to the `project/` folder.
2. Install the required dependencies.

### Using `pip`:
Install dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Using `conda`:
Alternatively, create a Conda environment and install the required packages:

```bash
conda create --name <environment-name> --file requirements.txt
```

*Note*: Some packages are only available through `conda-forge`, and others must be installed with `pip`, as specified in the `requirements.txt` comments.

---

## Contact

For any questions or further information, please reach out to **Céaman Collins** via GitHub.

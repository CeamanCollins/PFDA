# PFDA Project

This folder contains the project for the module Programming for Data Analytics at ATU.

## Brief

Write a Notebook that demonstrates that you can perform data analysis on some
data.

## Summary of Project

This project provides a comprehensive analysis of wind speed data from Mace Head Atmospheric Research Station on the west coast of Ireland, with implications for wind energy generation.

**Key Findings:**

1. **Storm Analysis**: The investigation identified and visualized six major storm events recorded at Mace Head, demonstrating the station's capability to capture significant weather phenomena.

2. **Wind Turbine Viability**: Wind turbines with typical specifications would be operational approximately 90% of the time at Mace Head, exceeding the industry standard of 85%. However, only 0.03% of recorded wind speeds exceed the maximum safe operating threshold, indicating the location is well-suited for wind energy development.

3. **Seasonal Patterns**: Analysis revealed distinct seasonal wind speed variations, with consistent patterns across years. Monthly wind speeds showed clear periodicity, with higher winds expected during winter months and lower speeds during summer.

4. **Comparative Analysis**: Among Irish weather stations surveyed, Mace Head ranked as the second-best location for wind turbine operation, surpassed only by Malin Head. This positions the station as an excellent candidate for wind farm development.

5. **Power Generation Potential**: Using a 48-meter diameter turbine model, estimated power output calculations suggest the location could generate approximately **3.50 MWh in January 2026** alone, with strong potential for consistent year-round energy production.

6. **ARIMA Forecasting Model**: The developed ARIMA(2,0,2) seasonal model successfully captured monthly wind speed patterns with high accuracy, achieving only 3% difference between predicted and actual values in the test set. The model exhibits strong potential for medium-term forecasting.

**Conclusion**: In conclusion, the ARIMA model developed in this analysis successfully predicts monthly average wind speeds and demonstrates Mace Head's strong potential for wind energy generation. The model captures seasonal patterns with exceptional accuracy and provides reliable forecasts for planning wind farm operations. How well these predictions perform for future conditions will provide valuable validation for long-term renewable energy planning at this location.

## Requirements

There is a [requirements.txt](requirements.txt) file that contains the necessary packages for the execution of code contained in this notebook. If using conda, some are only available through conda-forge and some are not available through conda and can only be accessed through pip. Please refer to the comments in the requirements file for more information.

## Use

The project is contained within a Jupyter notebook. You can open this in VSCode, on a Jupyter server on your own machine or in codespaces on GitHub. The code is designed to be run in sequence and may not run if you attempt to run single cells out of sequence.
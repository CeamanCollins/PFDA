# PFDA Project

This folder contains the project for the module Programming for Data Analytics at ATU.

## Brief

Write a Notebook that demonstrates that you can perform data analysis on some
data.

## Summary of Project

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

## Requirements

There is a [requirements.txt](requirements.txt) file that contains the necessary packages for the execution of code contained in this notebook. If using conda, some are only available through conda-forge and some are not available through conda and can only be accessed through pip. Please refer to the comments in the requirements file for more information.

## Use

The project is contained within a Jupyter notebook. You can open this in VSCode, on a Jupyter server on your own machine or in codespaces on GitHub. The code is designed to be run in sequence and may not run if you attempt to run single cells out of sequence.
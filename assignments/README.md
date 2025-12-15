# Programming for Data Analytics: Assignments

Author: Céaman Collins

This folder contains the assignments for the module Programming for Data Analytics at ATU.

There is a requirements text in this folder, which are required to run the code.

It can be run in codespaces or cloned to be run in VSCode or Jupyter Notebook.

## Contents

### Assignment 2: Northern bank holidays

In this assignment were were asked to create a script that would print out the dates of the bank holidays that happen in Northern Ireland by reading in data from a JSON file on the UK government website. In order to get the last few marks we were asked to print the bank holidays that are unique to Northern Ireland.

> Write a program called assignment02-bankholdiays.py
>
> The program should print out the dates of the bank holidays that happen in northern Ireland.
>
> Last few marks (ie this is more tricky)
>
> Modify the program to print the bank holidays that are unique to northern Ireland (i.e. do not happen elsewhere in the UK) you can choose if you want to use the name or the date of the holiday to decide if it is unique.

### Assignment 3: Domains

In this assignment we were asked to create a pie chart of the email domains of users' emails contained in a csv file. 

> Create a notebook called assignment03-pie.ipynb
> 
> The note book should have a nice pie chart of peoples email domains in the csv file at the url
> 
> https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download
> 
> This csv file has 1000 people. You may download the data or link to it.
> 
> Marks will be given for:
> 
> Just creating the pie chart
> Making it look nice
> As always your code should be well laid out.
> 
> If you are having difficulties, know I will be doing more on Pie charts later in this module.

### Assignment 5: 

In this assignment we were asked to analyse some data from the Central Statistics Office of Ireland and look at the population distribution of male and females around the country, in various stratifications and forms.

> This assignment is broken into 3 parts
> 
> Upload the notebook assignment05-population.ipynb to you assignments repository.
> 
> #### Part 1 70%
> Write a jupyter notebook that analyses the differences between the sexes by age in Ireland.
> 
> Weighted mean age (by sex)
> The difference between the sexes by age
> This part does not need to look at the regions.
> 
> ie You can take the notebook I used in the lectures and substitute the sexes for the regions.
> 
> #### Part 2 20%
> In the same notebook, make a variable that stores an age (say 35).
> 
> Write that code that would group the people within 5 years of that age together, into one age group 
> 
> Calculate the population difference between the sexes in that age group.
> 
> #### Part 3 10%
> In the same notebook.
> 
> Write the code that would work out which region in Ireland has the biggest population difference between the sexes in that age group

### Assignment 6: Knock airport Weather

In this assignment, were were asked to analyse some data from Knock airport weather station and plot various details contained within the dataset linked.

> Create a notebook called assignment_6_Weather.ipynb
> 
> Get the data from this link.
> 
> https://cli.fusio.net/cli/climate_data/webdata/hly4935.csv
> 
> (This is different that the data I used in the lecture)
> 
> Plot:
> 
> The temperature
> The mean temperature each day
> The mean temperature for each month
> 60% of the marks will be given for the above
> 
> For the last 40%
> 
> Plot:
> 
> The Windspeed (there is data missing from this column)
> The rolling windspeed (say over 24 hours)
> The max windspeed for each day
> The monthly mean of the daily max windspeeds (yer I am being nasty here)
> You do not need to over comment your code. Marks will be given for how nice the plots are.
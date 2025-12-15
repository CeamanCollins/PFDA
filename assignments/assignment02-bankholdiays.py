# Assignment 02: Bank Holidays in Northern Ireland
# This script fetches and displays bank holidays in Northern Ireland,
# and identifies those unique to Northern Ireland compared to England, Wales, and Scotland.

#Author: Céaman Collins

# Import the requests library to handle HTTP requests
import requests

# Fetch bank holiday data from the UK government API
bank_holidays_url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(bank_holidays_url)
data = response.json()

# Extract holiday events for Northern Ireland, England & Wales, and Scotland
northern_ireland_holidays = data["northern-ireland"]["events"]
england_wales_holidays = data["england-and-wales"]["events"]
scotland_holidays = data["scotland"]["events"]

# Display holidays in Northern Ireland
print("Holidays in Northern Ireland:\n")
print("Title\t\t\t\t\tDate")
print("----------------------------------------------------")
for holiday in northern_ireland_holidays:
    # Format output based on title length for better alignment
    if len(holiday["title"]) <= 15:
        print(holiday["title"] + "\t\t\t\t" + holiday["date"])
    elif 15 < len(holiday["title"]) <= 23:
        print(holiday["title"] + "\t\t\t" + holiday["date"])
    else:
        print(holiday["title"] + "\t" + holiday["date"])
print("\n")

# Identify and display holidays unique to Northern Ireland
print("The following holidays are unique to Northern Ireland:\n")
print("Title\t\t\t\t\tDate")
print("----------------------------------------------------")
for holiday in northern_ireland_holidays:
    # Check if the holiday is not in England & Wales or Scotland
    if holiday not in england_wales_holidays \
    and holiday not in scotland_holidays:
        if len(holiday["title"]) > 23:
            print(holiday["title"] + "\t" + holiday["date"])
        else: 
            print(holiday["title"] + "\t\t\t" + holiday["date"])
        
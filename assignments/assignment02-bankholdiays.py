# Assignment 02: Bank Holidays in Northern Ireland
# This script fetches and displays bank holidays in Northern Ireland,
# and identifies those unique to Northern Ireland compared to England, Wales, and Scotland.

#Author: Céaman Collins

import requests

bank_holidays_url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(bank_holidays_url)
data = response.json()
northern_ireland_holidays = data["northern-ireland"]["events"]
england_wales_holidays = data["england-and-wales"]["events"]
scotland_holidays = data["scotland"]["events"]

print("Holidays in Northern Ireland:\n")
print("Title\t\t\t\t\tDate")
print("----------------------------------------------------")
for holiday in northern_ireland_holidays:
    if len(holiday["title"]) <= 15:
        print(holiday["title"] + "\t\t\t\t" + holiday["date"])
    elif 15 < len(holiday["title"]) <= 23:
        print(holiday["title"] + "\t\t\t" + holiday["date"])
    else:
        print(holiday["title"] + "\t" + holiday["date"])
print("\n")
print("The following holidays are unique to Northern Ireland:\n")
print("Title\t\t\t\t\tDate")
print("----------------------------------------------------")
for holiday in northern_ireland_holidays:
    if holiday not in england_wales_holidays \
    and holiday not in scotland_holidays:
        if len(holiday["title"]) > 23:
            print(holiday["title"] + "\t" + holiday["date"])
        else: 
            print(holiday["title"] + "\t\t\t" + holiday["date"])
        
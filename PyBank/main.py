# Imports
import os
import csv

# Count months

file = open("budget_data.csv")
reader = csv.reader(file)
months = len(list(reader))

# Sum total profit/loss

file = open("budget_data.csv")
reader = csv.DictReader(file)
profit = 0
profit = sum(float(row["Profit/Losses"]) for row in reader)

# Find greatest increase

file = open("budget_data.csv")
reader = csv.DictReader(file)
greatest_increase = 0
greatest_increase = max(float(row["Profit/Losses"]) for row in reader)

# Find greatest decrease

file = open("budget_data.csv")
reader = csv.DictReader(file)
greatest_decrease = 0
greatest_decrease = min(float(row["Profit/Losses"]) for row in reader)

# Print results (month - 1 to exclude headers)

print("Financial Analysis")
print ("Months: ", (months - 1))
print ("Total Profit/Loss: ", (profit))
print ("Average Change: ", profit / (months - 1))
print ("Greatest Increase ", greatest_increase)
print ("Greatest Decrease ", greatest_decrease)

with open("output.txt", "w") as text_file:
    print(f"Months: ", (months - 1),
    "Total Profit/Loss", (profit),
    "Average Change: ", (profit / (months - 1)),
    "Greatest Increase: ", (greatest_increase),
    "Greatest Decrease: ", (greatest_decrease),
    file=text_file)
# Imports
import os
import csv

file = open("budget_data.csv")
reader = csv.reader(file)
months = len(list(reader))

file = open("budget_data.csv")
reader = csv.DictReader(file)
profit = 0
profit = sum(float(row["Profit/Losses"]) for row in reader)

file = open("budget_data.csv")
reader = csv.DictReader(file)
greatest_increase = 0
greatest_increase = max(float(row["Profit/Losses"]) for row in reader)

file = open("budget_data.csv")
reader = csv.DictReader(file)
greatest_decrease = 0
greatest_decrease = min(float(row["Profit/Losses"]) for row in reader)

print("Financial Analysis")
print ("Months: ", (months - 1))
print ("Total Profit/Loss: ", (profit))
print ("Average Change: ", profit / (months - 1))
print ("Greatest Increase ", greatest_increase)
print ("Greatest Decrease ", greatest_decrease)
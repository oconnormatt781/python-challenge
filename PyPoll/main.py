# Imports
import os
import csv
import collections

Khan = 0
Correy = 0
Li = 0
OTooley = 0

file = open("election_data.csv")
reader = csv.reader(file)
votes = len(list(reader))

my_reader = csv.reader(open("election_data.csv"))
khanvotes = 0
for record in my_reader:
    if record[1] == "Khan":
        khanvotes += 1

from collections import Counter
Candidate = [rec[3] for rec in my_reader]
result = Candidate.count('Khan')
print(result)

print("Total Votes: ", votes - 1)
print("Khan Votes: ", khanvotes)

with open("output.txt", "w") as text_file:
    print(f"Total Votes:", (votes - 1),
    "Khan Votes: ", (khanvotes),
    file=text_file)
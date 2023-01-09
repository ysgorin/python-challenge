# PyPoll Challenge

import os
import csv

ttl_votes = 0
candidates = []

# File path of election data
resource_path = os.path.join("Resources", "election_data.csv")

# File path to export analysis
output_path = os.path.join("analysis", "analysis.txt")

with open(resource_path, 'r', encoding='utf') as data:
    csvreader = csv.reader(data, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        ttl_votes = ttl_votes + 1
        if row[2] not in candidates:
            candidates.append(row[2])

print(ttl_votes)
print(candidates)

# The dataset is composed of three columns: "Voter ID", "County", and "Candidate".
# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote

# Your analysis should align with the following results:

# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------
# In addition, your final script should both
# print the analysis to the terminal and export a text file with the results.
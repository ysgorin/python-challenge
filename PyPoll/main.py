# PyPoll Challenge

import os
import csv

ttl_votes = 0
dict_candidates = {}

# File path of election data
resource_path = os.path.join("Resources", "election_data.csv")

# File path to export analysis
output_path = os.path.join("analysis", "analysis.txt")

with open(resource_path, 'r', encoding='utf') as data:
    csvreader = csv.reader(data, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        ttl_votes = ttl_votes + 1
        if row[2] not in dict_candidates:
            dict_candidates[row[2]] = 0
        dict_candidates[row[2]] = dict_candidates[row[2]] +1

print(f"""
Election Results
-------------------------
Total Votes: {ttl_votes}
-------------------------""")
for k, v in dict_candidates.items():
    print(f"{k}: {round(((v/ttl_votes)*100),3)}% ({v})")
print(f"""-------------------------
Winner: {max(dict_candidates, key=dict_candidates.get)}
-------------------------""")

with open(output_path, 'a') as a:
    print(f"""Election Results
-------------------------
Total Votes: {ttl_votes}
-------------------------""", file=a)
    for k, v in dict_candidates.items():
        print(f"{k}: {round(((v/ttl_votes)*100),3)}% ({v})", file=a)
    print(f"""-------------------------
Winner: {max(dict_candidates, key=dict_candidates.get)}
-------------------------""", file=a)
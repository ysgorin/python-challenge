# PyPoll Challenge

import os
import csv

# Total Votes
ttl_votes = 0
# Dictionary - Candidate Name, Votes Won
dict_candidates = {}

# File path of election data
resource_path = os.path.join("Resources", "election_data.csv")
# File path to export analysis
output_path = os.path.join("analysis", "analysis.txt")

# Analyze election dataset
with open(resource_path, 'r', encoding='utf') as data:
    csvreader = csv.reader(data, delimiter=',')
    
    # Store the header row
    csv_header = next(csvreader)

    for row in csvreader:
        # Calculate total votes
        ttl_votes = ttl_votes + 1
        if row[2] not in dict_candidates:
            # Create dictionary key for identified candidate and start votes won tally
            dict_candidates[row[2]] = 0
        # Add one to the candidate's votes tally
        dict_candidates[row[2]] = dict_candidates[row[2]] +1

# Print election results to terminal
print(f"""
Election Results
-------------------------
Total Votes: {ttl_votes}
-------------------------""")
for k, v in dict_candidates.items():
    # Candidates Name: Percent of Votes Won (Number of Votes Won)
    print(f"{k}: {round(((v/ttl_votes)*100),3)}% ({v})")
# Candidate with the most votes won
print(f"""-------------------------
Winner: {max(dict_candidates, key=dict_candidates.get)}
-------------------------""")

# Print election results to .txt file
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
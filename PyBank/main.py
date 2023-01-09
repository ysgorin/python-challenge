# PyBank Challenge

import os
import csv

# Total Number of Months
ttl_mos = 0

# List of Months
mos = []

# Net Total of Profits/Losses
pnl_ttl = 0

# Previous Month's Profit/Loss
prev_amt = 0 

# List of Monthly Change in Profits/Losses
pnl_changes = []

# File path of financial dataset
resource_path = os.path.join("Resources", "budget_data.csv")

# File path to export analysis
output_path = os.path.join("analysis", "analysis.txt")

# Analyze financial dataset
with open(resource_path, 'r', encoding='utf') as file:
   csvreader = csv.reader(file, delimiter=",")
   
   # Store the header row
   csv_header = next(csvreader)

   for row in csvreader:
        # Calculate total months
        ttl_mos = ttl_mos +1
        
        # Create list of months
        mos.append(row[0])
        
        # Calculate net total of profits/losses
        pnl_ttl = pnl_ttl + int(row[1])
        
        # Calculate monthly change in profits/losses
        change = int(row[1]) - prev_amt
        
        # Create list of monthly changes
        pnl_changes.append(change)
        
        # Set previous amount variable for next row
        prev_amt = int(row[1])

# Analyze monthly changes in profits/losses
# Remove first values from pnl_changes and mos.
pnl_changes.pop(0)
mos.pop(0)

# Calculate average change
avg_change = round((sum(pnl_changes)/len(pnl_changes)),2)

# Calculate greatest increase and decrease
gr_inc = max(pnl_changes)
gr_dec = min(pnl_changes)

# Identify month of greatest increase and decrease
pnl_changes_and_mos = zip(mos, pnl_changes)
for row in pnl_changes_and_mos:
   if row[1] == gr_inc:
       gr_inc_mo = row[0]
   elif row[1] == gr_dec:
       gr_dec_mo = row[0]

# Print analysis results to terminal
print(f"""
Financial Analysis
----------------------------
Total Months: {ttl_mos}
Total: ${pnl_ttl}
Average Change: ${avg_change}
Greatest Increase in Profits: {gr_inc_mo} (${gr_inc})
Greatest Decrease in Profits: {gr_dec_mo} (${gr_dec})
""")

# Print analysis results to .txt file
with open(output_path, 'w') as a:
   print(f"""Financial Analysis
----------------------------
Total Months: {ttl_mos}
Total: ${pnl_ttl}
Average Change: ${avg_change}
Greatest Increase in Profits: {gr_inc_mo} (${gr_inc})
Greatest Decrease in Profits: {gr_dec_mo} (${gr_dec})""", file=a)
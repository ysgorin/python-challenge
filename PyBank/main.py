# In this Challenge, you are tasked with creating a Python script
# to analyze the financial records of your company.
# You will be given a financial dataset called budget_data.csv.
# The dataset is composed of two columns: "Date" and "Profit/Losses".

# Your task is to create a Python script that analyzes the records
# to calculate each of the following values:

import os
import csv

total_months = 0
months = []
net_profit_losses = 0
previous_amount = 0 
changes = []

resource_path = os.path.join("Resources", "budget_data.csv")

with open(resource_path, 'r', encoding='utf') as file:
    csvreader = csv.reader(file, delimiter=",")
    
    csv_header = next(csvreader)
    print(csv_header)

    # Get a sense of the data.
    # print(next(csvreader))
    # print(next(csvreader))
    # print(next(csvreader))

    for row in csvreader:
        total_months = total_months +1
        months.append(row[0])
        net_profit_losses = net_profit_losses + int(row[1])
        change = int(row[1]) - previous_amount
        changes.append(change)
        previous_amount = int(row[1])

# remove first change from changes because it is the first value.
# remove first month for same reason
changes.pop(0)
months.pop(0)
average_change = round((sum(changes)/len(changes)),2)
greatest_increase = max(changes)
greatest_decrease = min(changes)

changes_and_months = zip(months, changes)

for row in changes_and_months:
    if row[1] == greatest_increase:
        g_increase_month = row[0]
    elif row[1] == greatest_decrease:
        g_decrease_month = row[0]

# print(total_months)
# print(net_profit_losses)
# print(average_change)
# print(f"{g_increase_month} - {greatest_increase}")
# print(f"{g_decrease_month} - {greatest_decrease}")

print(f"""

Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_profit_losses}
Average Change: ${average_change}
Greatest Increase in Profits: {g_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {g_decrease_month} (${greatest_decrease})

""")

output_path = os.path.join("analysis", "analysis.txt")
with open(output_path, 'w') as a:
    print(f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_profit_losses}
Average Change: ${average_change}
Greatest Increase in Profits: {g_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {g_decrease_month} (${greatest_decrease})""", file=a)

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

# Your analysis should align with the following results:

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
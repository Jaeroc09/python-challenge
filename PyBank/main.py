# Import modules
import os
import csv

# Initialize variables
mo_yr = [] # Date list
mo_yr_pl = [] # Profit/Loss list
change_pl_MoM = [0] # Change in P/L Month over Month list; index 0 added as filler; remove when averaging list
min_index = 0 # list index for Greatest Increase in Profits
max_index = 0 # list index for Greatest Decrease in Profits

# Read path (PyBank/Resources/budget_data.csv)
read_path = os.path.join('.', 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(read_path, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader) # Header row
    
    for row in csvreader:
        mo_yr.append(row[0])
        mo_yr_pl.append(int(row[1])) # cast to integers
        
# START Analysis code block
total_mo = len(mo_yr)
total_pl = sum(mo_yr_pl)

for x in range(1,len(mo_yr_pl)):
    # Calculate profit/loss change Month over Month and append to list
    temp_change = mo_yr_pl[x] - mo_yr_pl[x - 1]
    change_pl_MoM.append(temp_change)
    
    # Track indexes for greatest profit and loss data
    if change_pl_MoM[x] > change_pl_MoM[max_index]:
        max_index = x
    elif change_pl_MoM[x] < change_pl_MoM[min_index]:
        min_index = x
    
# Calculate average of change list
# sliced from index 1 since 0 is a filler for index tracking
avg_change = round((sum(change_pl_MoM[1:])/len(change_pl_MoM[1:])), 2)

# END Analysis code block

# Terminal print-out
print("Financial Analysis\n-----------------------------")
print(f"Total Months: {total_mo}")
print(f"Total: ${total_pl}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {mo_yr[max_index]} (${change_pl_MoM[max_index]})")
print(f"Greatest Decrease in Profits: {mo_yr[min_index]} (${change_pl_MoM[min_index]})")

# Output summary to a text file in the 'analysis' folder
write_path = os.path.join('.','analysis','budget_analysis.txt')

with open(write_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n-----------------------------\n")
    txtfile.write(f"Total Months: {total_mo}\n")
    txtfile.write(f"Total: ${total_pl}\n")
    txtfile.write(f"Average Change: ${avg_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {mo_yr[max_index]} (${change_pl_MoM[max_index]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {mo_yr[min_index]} (${change_pl_MoM[min_index]})\n")

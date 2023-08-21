# Import modules
import os
import csv

# Initialize variables
ballot_id = [] # column 0
county = [] # column 1
candidate = [] # column 2

# Read path (PyPoll/Resources/election_data.csv)
read_path = os.path.join('.','Resources','election_data.csv')

# Read in the CSV file
with open(read_path, 'r') as csvfile:
    
    # Split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader) # Header row
    
    for row in csvreader:
        ballot_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    
# Create unique list of candidates
candidate_list = []
for x in candidate:
    if x not in candidate_list:
        candidate_list.append(x)

# START Analysis code block
total_votes = len(ballot_id)
candidate_votes = []
candidate_pct = []

# Calculate vote count and percentage of votes for each candidate
for x in candidate_list:
    candidate_votes.append(candidate.count(x))
    percent = round((candidate.count(x) / total_votes * 100), 3)
    candidate_pct.append(percent)

winner_index = candidate_votes.index(max(candidate_votes)) # does not consider duplicates; use for/if to check for ties
# END Analysis code block

# Create a string list with the formatting and election results
# based on information from https://www.pythontutorial.net/python-basics/python-write-text-file/
linebreak = "-----------------------"
voter_summary = []
title = "Election Results"
voter_summary.append(title)
voter_summary.append(linebreak)
voter_summary.append(f"Total Votes: {total_votes}")
voter_summary.append(linebreak)
for x in range(len(candidate_list)):
    voter_summary.append(f"{candidate_list[x]}: {candidate_pct[x]}% ({candidate_votes[x]})")
voter_summary.append(linebreak)
voter_summary.append(f"Winner: {candidate_list[winner_index]}")
voter_summary.append(linebreak)

# Terminal print-out of list
for x in voter_summary:
    print(x)

# Output results to a text file in the 'analysis' folder
write_path = os.path.join('.','analysis','election_results.txt')

with open(write_path, 'w') as txtfile:
    txtfile.write('\n'.join(voter_summary))

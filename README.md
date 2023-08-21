# python-challenge
The first of many projects using Python!
by Jason Estrada

There are two scripts created to analyze data from .csv files and then output the analysis to a text file (as well as to the terminal).  Changes were pushed to GitHub using terminal commands.

PyBank
Create a Python script to analyze the financial records of your company. The set of financial data is called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: "Date" and "Profit/Losses".
Analyze the records to calculate each of the following:
* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* The changes in "Profit/Losses" over the entire period, and then the average of those changes
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in profits (date and amount) over the entire period
Print the results to the terminal and also export them to a text file in the 'analysis' folder.

PyPoll
A set of poll data is given, called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Ballot ID", "County", and "Candidate". Create a Python script that analyzes the votes and calculates each of the following:
* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote.
Print the results to the terminal and also export them to a text file in the 'analysis' folder.

This challenge showcased the use of:
* handling big datasets with Python scripts as opposed to using Excel
* importing modules
* reading .csv files and writing to files
* storing content in variables, lists
* iterate through basic data structures
* backing up work (pushes) to GitHub
* for `PyBank`, analysis export to file was performed simply using `.write()` method for each line of string
* for `PyPoll`, analysis export to file was changed to store each line of string in a string list and writing each line with a for loop
* for `PyPoll`, no additional checks for duplicate Ballot IDs were performed, however can add this test in a later iteration with `set()` and comparing the length of the lists

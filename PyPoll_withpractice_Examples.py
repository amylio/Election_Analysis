# The data that we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote
# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
# To do: perform analysis.
    #print(election_data)
# to do: read and analyze data here
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print the header row.
    headers = next(file_reader)
    print(headers)
#Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
# Close the file.
# election_data.close()
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")
#with open(file_to_save,"w") as txt_file:
# Using the with statement open the file as a text file
# outfile = open(file_to_save,"w")
# Write some data to the file.
# outfile.write("Hello World")
   # txt_file.write("Hello World")
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")
    # or
    # txt_file.write("Arapahoe, Denver, Jefferson")
    #txt_file.write("\nArapahoe\nDenver\nJefferson")
    #txt_file.write("Counties in the Elections\n----------------------\nArapahoe\nDenver\nJefferson")
# Close the file
# outfile.close()

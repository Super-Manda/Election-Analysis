# Add our dependencies.
import csv
import os

# 3.4.1 Import the datetime class from the datetime module.
import datetime as dt

# 3.4.1 Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()

# 3.4.1 Print the present time.
print("The time right now is ", now)

# 3.4.2 Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# (previous method overwritten in module 3.4.2 was: file_to_load = 'Resources/election_results.csv')

# 3.4.2 Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # 3.4.3 Assign a variable to save the file to a path.
    file_to_save = os.path.join("analysis", "election_analysis.txt")

    # 3.4.4 will go here - To do: perform analysis - read and analyze data here.
    # 3.4.2 Print the file object.
    print(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)

# 3.4.2 replaces the below Close the File statement with a With statement
# election_data.close()

# 3.4.3 Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")

# 3.4.3 Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # 3.4.3 Write some data to the file.
    # overwritten - outfile.write("Hello World")
    # 3.4.3 Overwritten: Write three counties to the file on the same line.
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")
    # 3.4.3 Write three counties to the file on new lines.
    txt_file.write("Arapahoe\nDenver\nJefferson")

# 3.4.3 Close the file
outfile.close()

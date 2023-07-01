from logging import PercentStyle
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#sets initial variables
totalvote = 0
Candidatelist = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
candidate_votes = [0, 0, 0]
percentagevote = [0, 0, 0]
winner = "none"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    print(csvreader)

    #skips header row
    next(csvreader)

    for row in csvreader:
        #The total number of votes cast
        totalvote += 1

        # Determines the total number of votes each candidate received
        candidate = row[2]
        
        if candidate == Candidatelist[0]:
            candidate_votes[0] += +1
        if candidate == Candidatelist[1]:
            candidate_votes[1] += +1
        if candidate == Candidatelist[2]:
            candidate_votes[2] += +1

# Calculates the percentage vote for each candidate
for i in range (3):
    percentage = (candidate_votes[i] / totalvote) * 100
    percentagevote[i] = round(percentage, 3)
    # Determines the winner
    if candidate_votes[i] > candidate_votes[i - 1]:
        winner = Candidatelist[i]
        
#Prints the values

print("Election Results")

print("------------------------")

print("Total Votes: " + str(totalvote))

print("------------------------")

for i in range (3):
    print(str(Candidatelist[i]) + " : " + str(percentagevote[i]) + "% (" + str(candidate_votes[i]) + ") ")

print("------------------------")

print("Winner: " + winner)

print("------------------------")

file_path = ('analysis/analysis.txt')
with open(file_path, 'w') as file:
    file.write('Election Results\n')
    file.write("-----------------------------------------------------------------------\n")
    file.write("Total Votes: " + str(totalvote) + "\n")
    file.write("------------------------ \n")
    for i in range (3):
        file.write(str(Candidatelist[i]) + " : " + str(percentagevote[i]) + "% (" + str(candidate_votes[i]) + ") \n")
    file.write("------------------------\n")
    file.write("Winner: " + winner  + "\n")

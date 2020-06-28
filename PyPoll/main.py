import os
import csv

voting_csv_path = "../PyPoll/Resources/election_data.csv"

percent = []
cand_votes = []
candidates = []
total_votes = 0


with open(voting_csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
   
    for row in csvreader:
        total_votes += 1

        cand_row = (row[2])

        if cand_row in candidates:
            can_in = candidates.index(cand_row)
            cand_votes[can_in] = cand_votes[can_in] + 1
        else:
            candidates.append(cand_row)
            cand_votes.append(1)

    
max_votes = cand_votes[0]
max_in = 0

for i in range(len(candidates)):
    vote_percentage = (cand_votes[i]/total_votes * 100) 
    percent.append(vote_percentage)

    if cand_votes[i] > max_votes:
        max_votes = cand_votes[i]
        max_in = i
    
    election_winner = candidates[max_in]

print('                  Election Results                  ')
print('----------------------------------------------------')
print(f"Total Votes = {total_votes}")
print('---------------------------------------------------')
for i in range(len(candidates)):
    print(f"Top Candidate = {candidates[i]} : {percent[i]}% ({cand_votes[i]})")
print('---------------------------------------------------')
print(f"Election winner = {election_winner}")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
print(f"Total Votes =  {total_votes}", file=open('../PyPoll/Summary.txt', 'w'))
for i in range(len(candidates)):
    print(f"Top Candidate = {candidates[i]} : {percent[i]}% ({cand_votes[i]})", file=open('../PyPoll/Summary.txt', 'a'))
print(f"Winner=  {election_winner}", file=open('../PyPoll/Summary.txt', 'a'))

        
        










   

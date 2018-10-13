import os
import csv
import operator
import random
from collections import Counter
 

# Path to collect data from the Resources folder
Budget_Data = os.path.join('..', 'Resources', 'election_data.csv')


# Read in the CSV file
with open(Budget_Data, 'r') as csvfile:
    PyPoll = open('output.txt','w+')
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    votes = 0
    county = []
    voter_id = []
    candidate = []
    unique_candidates = []
    
    len_unique = len(unique_candidates)
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    
    sum_votes = len(voter_id)
    unique_candidates = list(set(candidate))
    len_unique = len(unique_candidates)
    print("Election Results")
    PyPoll.write('Election Results')
    print("---------------------------")
    PyPoll.write('\n' + '---------------------------')
    print(f"Total Votes : {sum_votes} ")
    PyPoll.write('\n' + 'Total Votes : ' + str(sum_votes))
    print("---------------------------")
    PyPoll.write('\n' + '---------------------------')
    prev_vote_count = 0

    for i  in range(0 , len_unique):
      candidate_listing = unique_candidates[i]
      candidate_vote_count=0
      for j in range(0, sum_votes):
            if candidate[j] == candidate_listing:
                candidate_vote_count +=1
      percent_votes = candidate_vote_count / sum_votes * 100
      if prev_vote_count < candidate_vote_count:
            prev_vote_count = candidate_vote_count
            prev_candidate = candidate_listing
      print(f"{candidate_listing}: {round(percent_votes, 2)} % ({candidate_vote_count}) ")
      PyPoll.write('\n' + candidate_listing + ' : ' + str(round(percent_votes,2)) + ' % ' + str(candidate_vote_count))
    print("---------------------------") 
    PyPoll.write('\n' + '---------------------------')
    print(f" Winner : {prev_candidate} ")
    PyPoll.write('\n' + 'Winner : ' + str(prev_candidate))
    print("---------------------------") 
    PyPoll.write('\n' + '---------------------------')
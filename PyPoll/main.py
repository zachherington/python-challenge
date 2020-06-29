# PyPoll Plan of Attack:
    # Resource data
    #   Col1: Voter ID (8 digits)
    #   Col2: County
    #   Col3: Candidate Name
    #
    # Deliverables:
    #   1.  The total number of votes cast
    #   2.  List of candidates that received a vote
    #   3.  Total votes for each candidate
    #   4.  % of total votes for each candidate
    #   5.  The greatest decrease in losses (date and amount) over the entire period
    #   6.  Write the results to a text file. 

 

# HW Attempt: PyPoll
# Import modules
import os
import csv

# Set the path
datapath = os.path.join('..','Resources', 'PyPoll_Data.csv')

# Read the csv data
with open(datapath) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    # Store header row
    headers = next(reader)

    # Store CSV data into
    voter_id_all = []
    county_all = []
    candidate_all = []

    # Create separate lists to store each category
    for row in reader:
        voter_id.append((row[0]))
        county.append((row[1]))
        candidate.append((row[2]))

# 1. Number of votes
    total_votes = len(voter_id)

# 2. Candidate List
    cand_list = list(set(candidate))
    total_cand = len(cand_list)
    # Store each name for reference
    cand1 = cand_list[0]
    cand2 = cand_list[1]
    cand3 = cand_list[2]
    cand4 = cand_list[3]
    
# 3. Total Votes by candidate
    cand1_votes = []
    cand2_votes = []
    cand3_votes = []
    cand4_votes = []
    
    for x in candidate_all:
        if x = cand1:
            cand1_votes.append
        if x = cand2:
            cand2_votes.append
        if x = cand3:
            cand3_votes.append
        if x = cand4:
            cand4_votes.append
    
    cand1_total = len(cand1_votes)
    


# 6. Print the results and write to txt file
    print("----------------------------")
    print("Election Results:")
    print("")
    print(f"Total Votes: {total_votes}")
    print(f"Total Candidates: {total_cand}")
    print("")
    # print(f"{cand1}: {cand1_per}% with {cand1_sum} votes.")
    # print(f"{cand2}: {cand1_per}% with {cand1_sum} votes.")
    # print(f"{cand3}: {cand1_per}% with {cand1_sum} votes.")
    # print(f"{cand4}: {cand1_per}% with {cand1_sum} votes.")
    print ("----------------------------")
    # print(f"Winner: {win_candidate}")
    print ("----------------------------")

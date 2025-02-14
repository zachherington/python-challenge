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
    #   5.  Determine the election winner
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

    # Create separate lists to store data
    voter_id_all = []
    county_all = []
    candidate_all = []

    # Append lists with column data
    for row in reader:
        voter_id_all.append((row[0]))
        county_all.append((row[1]))
        candidate_all.append((row[2]))

# 1. Number of votes
    total_votes = len(voter_id_all)

# 2. Candidate List
    cand_list = list(set(candidate_all))
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
    
    # Store total votes for each candidate into their own lists
    for x in candidate_all:
        if x == cand1:
            cand1_votes.append(x)
        if x == cand2:
            cand2_votes.append(x)
        if x == cand3:
            cand3_votes.append(x)
        if x == cand4:
            cand4_votes.append(x)
    
    # Take the length of each candidate's list to get a total # votes
    cand1_total = len(cand1_votes)
    cand2_total = len(cand2_votes)
    cand3_total = len(cand3_votes)
    cand4_total = len(cand4_votes)

# 4. Percent Votes by candidate 
    cand1_per = round((cand1_total / total_votes) *100 , 2)
    cand2_per = round((cand2_total / total_votes) *100 , 2)
    cand3_per = round((cand3_total / total_votes) *100 , 2)
    cand4_per = round((cand4_total / total_votes) *100 , 2)

# 5. Determine the election winner
    # Dictionary to store candidate name (key) and vote total (value)
    candidate_results = {   cand1 : cand1_total, 
                            cand2 : cand2_total, 
                            cand3 : cand3_total, 
                            cand4 : cand4_total}

    # finds the max value in candidate results and returns the Name (key)
    winner = max(candidate_results, key = candidate_results.get)
    

# 6. Print the results and write to txt file
    print("----------------------------")
    print("Election Results:")
    print("")
    print(f"Total Votes: {total_votes}")
    print(f"Total Candidates: {total_cand}")
    print("----------------------------")
    print(f"{cand1}: {cand1_per}% with {cand1_total} votes.")
    print(f"{cand2}: {cand2_per}% with {cand2_total} votes.")
    print(f"{cand3}: {cand3_per}% with {cand3_total} votes.")
    print(f"{cand4}: {cand4_per}% with {cand4_total} votes.")
    print ("----------------------------")
    print(f"Winner: {winner}")
    print ("----------------------------")

    resultspath = os.path.join('..','Analysis', 'Results_pypoll.txt')
    with open(resultspath , "w") as text:
        text.write("----------------------------")
        text.write("\nElection Results:")
        text.write("\n")
        text.write(f"\nTotal Votes: {total_votes}")
        text.write(f"\nTotal Candidates: {total_cand}")
        text.write("\n----------------------------")
        text.write(f"\n{cand1}: {cand1_per}% with {cand1_total} votes.")
        text.write(f"\n{cand2}: {cand2_per}% with {cand2_total} votes.")
        text.write(f"\n{cand3}: {cand3_per}% with {cand3_total} votes.")
        text.write(f"\n{cand4}: {cand4_per}% with {cand4_total} votes.")
        text.write("\n----------------------------")
        text.write(f"\nWinner: {winner}")
        text.write("\n----------------------------")
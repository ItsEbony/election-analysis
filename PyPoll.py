# The data we need to retrieve. 
# 1. The total nmber of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#Add dependencies 
import csv
import os
#Connect source document (load a file from a path)
csvpath = os.path.join('/Users/ebonybrown/Desktop/Data Analysis Assignments/Election Analysis/election-analysis/Resources', 'election_results.csv')
#Connect output doc (save the file to a path)
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter. 
total_votes = 0

# Candidate Options
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open elections results and read the file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)

    # Read the header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #Print each row in CSV file
    for row in csvreader:
        # 2. add to the total vote count
        total_votes += 1
        
        # Print the candidate name from each row
        candidate_name = row[2]
        
        # If the candidate doesn't match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the candidate list
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #interate through the canddiate list 
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate 
        votes = candidate_votes[candidate_name]
        #calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #print the canddiate name and percentage of votes
        # to keep track of this operation if I need it: print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")
        
        # determine winning vote count and candidate
        # determine if the votes are greater than the winning count
        print(vote_percentage)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning count = votes and winning percentage = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #set the winning candidate equal to the candidate's name
            winning_candidate = candidate_name
#print winning candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

# 3. print candidate vote dictionary
print(candidate_votes)
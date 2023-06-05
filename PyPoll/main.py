# import modules
from pathlib import Path
import csv

# read csv file
csvpath = Path("Resources/election_data.csv")

with open(csvpath, encoding='UTF-8') as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")

    # Take out header row
    csv_header = next(election_data)

    # Set Variables
    voter_list = []
    candidate_vote = []
    unique_candidates = []
    vote_count = []
    percentage = []

    # Loop through data
    for row in election_data:
        # get relevant data and split them between voters and candidates
        voter_list.append(row[0])
        candidate_vote.append(row[2])

    # calculate total votes
    total_votes = len(voter_list)

    # Isolate unique candidates
    for candidate in set(candidate_vote):
        unique_candidates.append(candidate)
        vote_count.append(candidate_vote.count(candidate))

    # calculate percentage of votes
    for count in vote_count:
        percentage.append(round((count / sum(vote_count) * 100), 3))

    # calculate winner
    max_votes = max(vote_count)
    max_index = vote_count.index(max_votes)
    winner = unique_candidates[max_index]

    # print the results
    print("Election Results")
    print("\n")
    print("-------------------------")
    print("\n")
    print(f"Total Votes: {total_votes}")
    print("\n")
    print("-------------------------")
    print("\n")

    for i in range(len(unique_candidates)):
        print(f"{unique_candidates[i]}: {percentage[i]}% ({vote_count[i]})")
        print("\n")

    print("-------------------------")
    print("\n")
    print(f"Winner: {winner}")
    print("\n")
    print("-------------------------")

    # write to file
    output_path = Path("analysis/Poll_Results.txt")
with open(output_path, 'w') as file:
    file.write("Election Results")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    for i in range(len(unique_candidates)):
        file.write(f"{unique_candidates[i]}: {percentage[i]}% ({vote_count[i]})")
        file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write("-------------------------")

    file.close





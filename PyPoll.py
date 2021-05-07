# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# Track winning candidate, vote count, and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote counter
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate name does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            # Begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    # Save the results to our text file
    with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal
        election_results = (
            f"\nElection Results\n"
            f"---------------------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"---------------------------------------\n"
        )

        print(election_results, end="")
        # Save the final votge count to the text file
        txt_file.write(election_results)

        # Determine the percentage of votes for each candidate by looping through the counts
        # Iterate through the candidate list
        for candidate_name in candidate_votes:
            # Retrieve vote count and percentage
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate's voter count and percentage
            print(candidate_results)

            # Save the results to our text file
            txt_file.write(candidate_results)

            # Determine winning vote count, winning percentage, and winning candidate
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true, set winning_count = votes and winning_percentage = vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                # Set winning_candidate = candidate's name
                winning_candidate = candidate_name

        # Print the winning candidate's results
        winning_candidate_summary = (
            f"---------------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------------------------"
        )

        print(winning_candidate_summary)

        # Save winning candidate's results to the text file
        txt_file.write(winning_candidate_summary)

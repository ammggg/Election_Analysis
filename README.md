# Election Analysis

## Project Overview
A Colorado Board of Elections employee has tasked me with the following in order to complete the audit of a recent local congressional election. 

1. Calculate the total number of votes cast.
2. Calculate a summary based on county.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.5, Visual Studio Code 1.56.0

## Election Audit Results
The analysis shows that:
- There were 369,711 votes cast in this election.
- County Results:
    - Jefferson County accounted for 10.5% of the vote and 38,855 number of votes.
    - Denver County accounted for 82.8% of the vote and 306,055 number of votes.
    - Arapahoe County accounted for 6.7% of the vote and 24,801 number of votes.
- Largest County Turnout:
    - Denver County, which received 82.8% of the vote and 306,055 number of votes.
- Candidate Results:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- Winner of the election:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Election Audit Summary
In conclusion, this has been a full and complete audit of the local congressional election which shows that Diana DeGette won the popular vote.

Going foward, this script can be useful in auditing any Colorado election, with some modifications. Currently, this code is set up to handle any number of candidates/reporting counties, with the assumption that the headers provided in the CSV file will not change - for example, the code is indexed to the current location for County and Candidate. Below is the specific lines of code tha relate to this indexing, beginning in row 48 of the script:

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

Additionally, if additional data were to be provided, such as sex, age, or perhaps level of education, you would need to modify the code further in order to incorporate and analyze this data. 

# Election Analysis 

## Candidates Overview
A Colorado Board of Elections employee has asked that we conduct an audit of a recent local congressional election. 

To complete this task, we will need to do the following: 

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidate received. 
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of the election based on the popular vote. 

### Resources
- Data Source: election_results.csv
- Software: Python 3.7.6

### Candidate Results
Our analysis of the election results found the following: 
- There were 369,711 votes cast in the election.
- The candidates were: 
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were: 
  - Charles Casper Stockham received 23.0% of the vote with 85,213 total votes.
  - Diana DeGette received 73.8% of the vote with 272,829 total votes.
  - Raymon Anthony Doane received 3.1% of the vote with 11,606 total votes.
- **The winner of the election was Diana DeGette, who received 73.8% of the vote with 272,829 total votes.**

## Voter Turnout Overview
The Colorado Board of Elections aslo asked that we analyze the voter turnout and break it down by the three counties that participated.

To meet the client's request, we had to do the following:
1. Calculate the total number of votes cast, which we were able to pull from the candidate analysis.
2. Identify the counties that voted in the election. 
3. Calculate how many votes were cast in each county. 
4. Determine which county had the highest voter turnout.

### Resources
- Data Source: election_results.csv
- Software: Python 3.7.6

### County Results
Looking at county turnout, our analysis found the following:
*Note: Based on the candidate analysis, we went into the county analysis knowing that 369,711 total votes were cast in the election.*
The participating counties were: 
- Jefferson
- Denver
- Arapahoe
Voter turnout for each county showed: 
- Jefferson accounted for 10.5% of total ballots with 38,855 votes.
- Denver accounted for 82.8% of total ballots with 306,055 votes.
- Arapahoe accounted for 6.7% of total ballots with 24,801 votes.

**Denver** had the highest voter turnout of the three counties. 

## Challenge Summary
This script can be modified to meet other needs that the Board of Elections may need, including: 
1. We could collect additional information from voters such as party affiliation or demographic data like age/race/gender and provide breakdowns of voter turnout for each of these groups and look at which groups voted for which candidate. 
2. The script could also be tweaked to account for additional counties for larger elections or elections in different parts of Colorado.

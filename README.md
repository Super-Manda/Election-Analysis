# Election Analysis in Python


## Overview of Project 
A Colorado Board of Elections employee initially assigned me this list of tasks in order to certify the election results of a recent local congressional district election that had collected ballots via mail (hand-counted), punch-card (machine counted), and electronic (computer counted) means:

1. Calculate the total number of votes cast;
2. Get a complete list of candidates who received notes;
3. Calculate the total number of votes each candidate received;
4. Calculate the percentage of votes each candidate won;
5. Determine the winner of the election based on popular vote.
6. As the challenge evolved, he also asked for voter turnout information in the counties.  

Due to the large size of the dataset and the various means by which the votes returned to Central Office, these findings were performed in Python, shown here: 
[PYPOLL CHALLENGE CODE](https://github.com/Super-Manda/Election-Analysis/blob/main/PyPoll_CHALLENGE.py)


## Resources 
**Original Data Source:** 
- [election_results.csv](https://github.com/Super-Manda/Election-Analysis/blob/main/Resources/election_results.csv)


**Softwares:** 
- Python 3.10 
- Visual Studio Code 1.68
- PyCharm 2022.1.2


## Election Audit Results
- A total of 369,711 votes were cast in this election.

- The contenders were: 
	- Diana DeGette, 
	- Charles Casper Stockham, and 
	- Raymon Anthony Doane.
	
- Denver County had the largest voter turnout.  In terms of the votes from the counties, Denver contributed 82.8% of the votes (306,055 votes).
- Arapahoe County had the smallest voter turnout, and only contributed 6.7% of the votes (24,801 votes).
- Jefferson County contributed 10.5% of the votes (38,855 votes).

The candidate results were:
  - Diana DeGette garnered 272,892 votes, which represented 73.8% of the total votes in this election.
  - Charles Casper Stockham garnered 85,213 votes, which represented 23.0% of the total votes in this election.
  - Raymon Anthony Doane garnered 11,606 votes, which represented 3.1% of the total votes in the election.  

-Diana DeGette won the election by a landslide because she received 272,892 votes (73.8% of the total votes).

The Python terminal prints this out as shown: 

![TERMINAL PRINTOUT](https://github.com/Super-Manda/Election-Analysis/blob/main/Analysis/Terminal%20Printout%20of%20Election%20Results.png)


## Election Audit Summary
The text file summarizes this current audit:
[TEXT FILE](https://github.com/Super-Manda/Election-Analysis/blob/main/Analysis/election_results.txt)

Furthermore, the election commission can use this script with some modifications for any election.  
- It could be expanded to other counties and other candidates, or to a larger number of them.  
- The script can be modified to see if voter turnout per county is typical or atypical for a given year.  For example, if it's a presidential election year or if a particular candidate is especially good or bad, it may affect how many voters come out.  In addition, there may be particular demographics or party affiliations who tend to vote more than others in each county.  This would require a historical dataset to be imported and compared to the present dataset. 
- Earlier in the module, the "datetime" function was used in previous versions of the file, so it would be possible to put that back into the present code so that it can be verified that the original analysis and the "recount" will come up with the same (or nearly the same) numbers in contested elections where the losing candidate is demanding a recount.  In this particular election, it was not necessary because the losing candidates lost by a large margin.  

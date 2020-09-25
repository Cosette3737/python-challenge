# import the os module
import os
#reading CSV File
import csv
csvpath=os.path.join("C:\\Users\\coset\\OneDrive\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv")
with open(csvpath,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header= next(csvreader)
        for x in csvreader:
            if votes>0:
                print_candidate(x)
                filename= 'Resources\election_data.csv.csv'


#create columns Voter ID, County, Candidate
name=str(election_data[2])
vote_ID=

#Analyze total number of votescast
#complete list of candidates who recieved votes
if float(row[])>0:
    print(candidate)
#percentage of votes each candidate won
# number of votes for each candidate
#winner of the electon on popular vote



}
#print to terminal
#print to text file

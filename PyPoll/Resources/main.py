#import the os module
import os
#reading CSV File
import csv

fileout=os.path.join("Election_Results.txt")
csvpath=os.path.join("Resources\election_data.csv.csv")
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        header=next(csvreader)
        csvpath=os.path.join("election_data.csv")
#variables
        counter=0
        votecount=[]
        smalllist=[]
        unicount=[]
        candidatestring=[]
        candidatelist=[]
#loop and get candidates
        for row in csvreader:
            counter = counter + 1
            candidate = (row[2])
            
    #create list of individual candidates
            if candidate in smalllist:
                candidate_index=smalllist.index(candidate)
                unicount[candidate_index]=unicount[candidate_index] +1
                
            else:
                smalllist.append(candidate)
                unicount.append(1)
#percentages
        percent=[]
        topvotes=unicount[0]
        topindex=0
        for x in range(len(smalllist)):
            percentage=round(unicount[x]/counter*100,2)
            percent.append(percentage)
            if unicount[x]>topvotes:
                topvotes=unicount[x]
                print(topvotes)
                topindex=x
        Winner=smalllist[topindex]
output1=(
    f"Election Results\n -------------\n"
    f"Total Votes: {counter}\n"
    f"-------------\n")

end=(
    f"\n-------------\n"
    f"Election Winner:{Winner.upper()}\n"
    f"-------------")

#WinnerList String
print(output1)
for x in range(len(unicount)):
    print(f'{smalllist[x]} : {percent[x]}%  ({unicount[x]})')

print(end)
    
#output to txt.file
with open(fileout, "w") as txt_file:
    txt_file.write(output1)
    for x in range(len(unicount)):
        txt_file.write(f'{smalllist[x]} : {percent[x]}%  ({unicount[x]})\n')
    txt_file.write(end)
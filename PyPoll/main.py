# import the os module
import os
#reading CSV File
import csv

#fileout=os.path.join("Election_Results.txt")
csvpath=os.path.join("election_data.csv")
#fileout=os.path.join("Election_Results.txt")

    
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        header=next(csvreader)
        csvpath=os.path.join("election_data.csv")
        counter=0
        votecount=[]
        smalllist=[]
        unicount=[]
        candidatestring=[]
#Total number of votes        
#totalvotes=sum(introw[1])
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

        percent=[]
        topvotes=unicount[0]
        topindex=0
        for count in range(len(smalllist)):
            percentage=round(unicount[count]/counter*100,2)
            percent.append(percentage)
            if unicount[count]>topvotes:
                topvotes=unicount[count]
                print(topvotes)
                topindex=count
                Winner=candidate[topindex]

        for x in range(len(smalllist)):
           x='{smalllist[x]} : {percent[x]}%  ({unicount[x])})'

output=(
f"Election Results\n -------------\n"
f"Total Votes: {counter}\n"
f"-------------\n"
f"x-------------\n"
f"Winner:{}\n"
f"-------------")
print(output)


#output to txt.file
with open(fileout, "w") as txt_file:
    txt_file.write(output)
  
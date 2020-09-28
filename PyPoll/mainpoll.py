# import the os module
import os
#reading CSV File
import csv

fileout=os.path.join("Election_Results.txt")


csvpath=os.path.join("election_data.csv")
#fileout=os.path.join("Election_Results.txt")
rawdata=['1','2']
for files in rawdata:
        csvpath=os.path.join("election_data.csv")
        candidates=[]
        votecount=[]
        counter=0
    
        with open(csvpath) as csvfile:
                csvreader = csv.reader(csvfile,delimiter=',')
                header=next(csvreader)


                totalvotes=sum(introw[1])
                print (totalvotes)
                for row in csvreader:
                        counter = counter + 1
                        candidate = str(csvpath[2])
                        votecount=0

                if candidate in candidates:
                        votecount+1
                        

                else:
                    candidates.append(candidate)
                    votecount+1

                percentage=
                
                percentages=[]
                VoteTotal=votecount[0]
                vote_index=0
        
               
                for count in range(len(candidates)):
                        percentage=votecount[count]/vote_number
                        percentage=percentage*100
                        percentages.append(percentage)
                     
                        if votecount[count]>VoteTotal:
                                VoteTotal=votecount[count]
                                print(votecount)
                                vote_index=count
                                print(VoteTotal)                
                                Winner=candidates[Vote-index]

        
        #variables
        for count in range(len(candidates)):
                Candidatestring="{candidates[count]}:{percentages[count]}%({votecount[count]})"

#display results
Output=(f"\nElection Results \n -----------\n"
        f"Total Votes:{VoteTotal}\n"
        f"-----------\n"
        f"{Candidatestring}\n"
        f"Winner:(Winner)\n"
        f"-----------")

#print results
print(Output)
#save to txt file
#with open(fileout, "W") as txt_file:
 #   txt_file.write(Output)
        
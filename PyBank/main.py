# import the os module
import os
#reading CSV File
import csv
csvpath=os.path.join("Budget_data.csv.csv")
fileout=os.path.join("Budget_analysis.txt")
#openfile
with open(csvpath,'r') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',')
      header = next(csvreader)
      #Variables
      profitchangelist=[]
      profits =[]
      date=[]
      counter=0
      Total_prof=0
      previous_revenue=867884
      profitchange=0
     
     
  #loop through file
      for row in csvreader:
            counter=1+counter
            date.append(str(row[0]))
            profits.append(int(row[1]))
            
            #get values for total month, total revenue
            total_months = len(date)
            NumberProfChange=total_months-1
            total_profit = sum(profits)

            #Get profitchangelist
            initialprofit=int(row[1])
            profitchange =initialprofit-previous_revenue
            previous_revenue=int(row[1])
            #get change average
            profitchangelist.append(profitchange)
            Totprofitchange=sum(profitchangelist)


changecount=round((Totprofitchange)/(NumberProfChange),2)
print(changecount)
            #Get the Greatest increase and Lowest increase
great_inc=max(profitchangelist)
great_index=profitchangelist.index(great_inc)
great_date=date[great_index]
low_inc=min(profitchangelist)
low_index=profitchangelist.index(low_inc)
low_date=date[low_index]

         
   #create text for file         
output=(      
f"Financial Analysis \n -------------\n"
f"Total Months:{total_months}\n"
f"Total: ${total_profit}\n"
f"Average Change: ${changecount}\n"
f"Greatest Increase in profits: {great_date} (${great_inc})\n"
f"Greatest Decrease in profits: {low_date} (${low_inc})")
     
print(output)
#output to txt.file
with open(fileout, "w") as txt_file:
    txt_file.write(output)
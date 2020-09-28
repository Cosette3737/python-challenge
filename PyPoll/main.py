
# import the os module
import os
#reading CSV File
import csv
csvpath=os.path.join("Resources\Budget_data.csv.csv")
fileout=os.path.join("Budget_analysis.txt")
with open(csvpath,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader)

        profits = []
        months = []

        for row in csvreader:
                profit = int(row[1])
                profits.append(profit)
                month = str(row[0])  
                months.append(month)

                total_months = len(profits)
                total_profit = sum(profits)
                month_change = [profits[i + 1] - profits[i] for i in range(len(profits)-1)]
                change_count = len(month_change)
                summonth=sum(month_change)
                total_change =round(summonth/(total_months))
                summonth=sum(month_change)
                #great_inc = max(month_change)
                #great_dec = min(month_change)
output=(      
      f"Financial Analysis \n -------------\n"
      f"Total Months:{total_months}\n"
      f"Total: ${total_profit}\n"
      f"Average Change: ${total_change}\n")
      #f"Greatest Increase in profits: {great_inc}\n")
      #f"Greatest Decrease in profits: {great_dec}"))

      #output to terminal
print(output)      
#output to txt.file
with open(fileout, "w") as txt_file:
    txt_file.write(output)
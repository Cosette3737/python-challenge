# import the os module
import os
#reading CSV File
import csv
csvpath=os.path.join("Resources\Budget_data.csv.csv")
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
                great_inc = max(month_change)
                great_dec = min(month_change)
        
print(f"Financial Analysis \n --------------")
print(f"Total Months:{total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${total_change}")
print(f"Greatest Increase in profits: {great_inc}")
print(f"Greatest Decrease in profits: {great_dec}")
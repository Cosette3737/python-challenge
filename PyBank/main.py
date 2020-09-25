# import the os module
import os
#reading CSV File
import csv
csvpath=os.path.join("C:\\Users\\coset\\OneDrive\\Desktop\\python-challenge\\PyBank\\Resources\\Budget_data.csv.csv")
with open(csvpath,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header= next(csvreader)
        for x in csvreader:
                filename= 'Resources\Budget_data.csv.csv'
                months = int(float(filename[0]) + 1
                print(months)
                total = int(float(filename[1])
                #return [total]
                #Analyze total Number of months
                #Months = int(float(1 for line in open(filename))-1)
                MonthNum = sum(months)
        #return [monthNum]
                print (f"Financial Analysis----------------Total Months: {int(MonthNum)}")
        #Analyze net total amount of profit/losses
                Total_Profit = total + 0
#Average of changes in profit losses
                Average_Profits= Total_Profit /monthNum
#greatest increase in profits Date and Amount
#greatest decrease in losses  date and amount
#print to terminal
        print(f"Financial Analysis----------------Total Months:{int(MonthNum)}")
        print(f"Total:+ {int(Total_Profit)}")
        print(f"Average Change: +{str(Average_Profits)}")
        print(f"Greatest INcrease in Profits:{str(Great_Month)}")
        print(f"Greatest Decrease in Profits:{str(Least_Month)}")

#export to txtfile
with open(output_file, "w",newline='') as datafile:
        datafile.write(Output)
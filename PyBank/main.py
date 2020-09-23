# import the os module
import os
#reading CSV File
import csv
csvpath=os.path.join("C:\\Users\\coset\\OneDrive\\Desktop\\python-challenge\\PyBank\\Resources\\Budget_data.csv.csv")
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")


#Analyze total Number of months
#with open('csvpath_file') as f:
 
 #   csv_reader=csv.reader(f)
  #  for row in csv_reader:
   #     pass
    #print(csv_reader.line_num)


#Analyze net total amount of profit/losses


#Average of changes in profit losses

#greatest increase in profits Date and Amount

#greatest decrease in losses  date and amount


#print to terminal


#export to txtfile

import os
import csv
import operator
import random
import pandas 

# Path to collect data from the Resources folder
Budget_Data = os.path.join('..', 'Resources', 'budget_data.csv')


# Read in the CSV file
with open(Budget_Data, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    profit_losses = 0
    prev_profit_loss = 0
    avg_diff = []
    month = []
    profit_loss = []
    max_profit_loss = 0
    min_profit_loss = 0
    
    # Loop through the data
    for row in csvreader:
        month.append(row[0])
        profit_loss.append(int(row[1]))
        diff_profit_loss = int(row[1]) - prev_profit_loss
        if prev_profit_loss != 0 :
            avg_diff.append(int(diff_profit_loss))
        if int(row[1]) < prev_profit_loss:
           min_profit_loss = int(row[1])
           min_pl_month = row[0]
        else:
           max_profit_loss = int(row[1])
           max_pl_month = row[0]
        prev_profit_loss = int(row[1])

    max_index = avg_diff.index(max(avg_diff)) + 1
    min_index = avg_diff.index(min(avg_diff)) + 1
    print("Financial Analysis")
    print("---------------------------")
    print(f" Total Months : {len(month)} ")
    print(f" Total : {sum(profit_loss)} ")
    print(f" Average Change : {sum(avg_diff)/(len(month)-1)} ")
    print(f" Greatest increase in profit : {str(month[max_index])} : ({max(avg_diff)}) ")
    print(f" Greatest decrease in profit : {str(month[min_index])} : ({min(avg_diff)}) ")
   
PyBank = open('output.txt','w+')
PyBank.write('Financial Analysis')
PyBank.write('\n' + '---------------------------')
PyBank.write('\n' + 'Total Months : ' + str(len(month)))
PyBank.write('\n' + ' Total : ' + str(sum(profit_loss)))
PyBank.write('\n' + ' Average Change : ' + str(sum(avg_diff)/(len(month)-1)))
PyBank.write('\n' + ' Greatest increase in profit : ' + str(month[max_index]) + ' : ' + str(max(avg_diff)))
PyBank.write('\n' + ' Greatest decrease in profit : ' + str(month[min_index]) + ' : ' + str(min(avg_diff)))

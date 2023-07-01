import os
import csv
from statistics import mean

csvpath = os.path.join('Resources', 'budget_data.csv')

#sets initial variables
month = 0
profit = 0
greatestprofit = 0
lowestprofit = 0
profitlist = []

# open the csv file and sets csvreader to the file with the comma being the delimiter
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

    print(csvreader)

    # skips the first header
    next(csvreader)

    # The total number of months included in the dataset
    for row in csvreader:
        month += 1
        # adds the value of row 1 into the profitlist
        profitlist.append(int(row[1]))

        # calculates the greatest profit value
        if int(row[1]) > greatestprofit:
            greatestprofit = int(row[1])

            # determines the month for greatest profit
            greatestprofitmonth = (row[0])
        
        # calculates the greatest total loss
        if int(row[1]) < lowestprofit:
            lowestprofit = int(row[1])

            #determines the month for the greatest total loss
            lowestprofitmonth = (row[0])

    # The changes in "Profit/Losses" over the entire period, and then the average of those changes

    averageprofit = mean(profitlist)

    # adds up all values in the profit list
    profit = sum(profitlist)
    
    # prints each value
    print("Financial Analysis")
    print("-----------------------------------------------------------------------")
    print("total amount of months: " + str(month))
    print("Total: $" + str(profit) + ".00")
    print("Average Change: $" + str(averageprofit) + ".00")
    print("Greatest increase in Profits: " + greatestprofitmonth + " ($" + str(greatestprofit) + " .00)")
    print("Greatest decrease in Profits: " + lowestprofitmonth + " ($" + str(lowestprofit) + " .00)")
    
    file_path = ('analysis/analysis.txt')
    with open(file_path, 'w') as file:
        file.write('Financial Analysis\n')
        file.write("-----------------------------------------------------------------------\n")
        file.write("Total amount of months: " + str(month) + "\n")
        file.write("Total : $ " + str(profit) + (".00") + "\n")
        file.write(" Average Change: $" + str(averageprofit) + ".00\n")
        file.write("Greatest increase in Profits: " + greatestprofitmonth + " ($" + str(greatestprofit) + " .00)\n")
        file.write("Greatest decrease in Profits: " + lowestprofitmonth + " ($" + str(lowestprofit) + " .00)\n")

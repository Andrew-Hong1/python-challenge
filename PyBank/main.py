import os
import csv
from statistics import mean

csvpath = os.path.join('Resources', 'budget_data.csv')

#sets initial variables
month = 0
profit = 0
greatestprofit = 0
lowestprofit = 0
change = 0
totalchange = 0
profitlist = []

# open the csv file and sets csvreader to the file with the comma being the delimiter
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

    print(csvreader)

    # skips the first header
    next(csvreader)

    previousrow = None

    # The total number of months included in the dataset
    for row in csvreader:
        month += 1
        # adds the value of row 1 into the profitlist
        profitlist.append(int(row[1]))

        # Calculate change
        if previousrow is not None:
            change = int(row[1]) - previousrow
            totalchange += change
            # Calculates greatest profit month and lowest profit month
            if change > greatestprofit:
                greatestprofit = change
                greatestprofitmonth = (row[0])
            if change < lowestprofit:
                lowestprofit = change
                lowestprofitmonth = (row[0])

        previousrow = int(row[1])

    # The changes in "Profit/Losses" over the entire period, and then the average of those changes

    averagechange = totalchange / (month - 1)

    # adds up all values in the profit list
    profit = sum(profitlist)
    
    # prints each value
    print("Financial Analysis")
    print("-----------------------------------------------------------------------")
    print("total amount of months: " + str(month))
    print("Total: $" + str(profit) + ".00")
    print("Average Change: $" + str(averagechange) + ".00")
    print("Greatest increase in Profits: " + greatestprofitmonth + " ($" + str(greatestprofit) + " .00)")
    print("Greatest decrease in Profits: " + lowestprofitmonth + " ($" + str(lowestprofit) + " .00)")
    
    file_path = ('analysis/analysis.txt')
    with open(file_path, 'w') as file:
        file.write('Financial Analysis\n')
        file.write("-----------------------------------------------------------------------\n")
        file.write("Total amount of months: " + str(month) + "\n")
        file.write("Total : $ " + str(profit) + (".00") + "\n")
        file.write(" Average Change: $" + str(averagechange) + ".00\n")
        file.write("Greatest increase in Profits: " + greatestprofitmonth + " ($" + str(greatestprofit) + " .00)\n")
        file.write("Greatest decrease in Profits: " + lowestprofitmonth + " ($" + str(lowestprofit) + " .00)\n")

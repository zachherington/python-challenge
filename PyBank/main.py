# PyBank: Plan of Attack
    # Data Callouts
    #   Col1: Date | MMM-YY | Min: 1/1/2010 | Max: 2/1/2017 |
    #   Col2: Profit/Losses | +/- # | Max: 1170593 | Min: -1196225 | 

    
    # Deliverables:
    #   1.  The total number of months included in the dataset
    #         Store all data into a dictionary
    #         Use the Len function on the dict to get total entries
      
    #   2.  The net total amount of "Profit/Losses" over the entire period
    #         use a for loop to cycle through each entry
    #         create a variable to store each entry
    #         redefine the variable for each entry by add

    #   3.  The average of the changes in "Profit/Losses" over the entire period
    #         Use the 2 variables above as the denominator and numerator respectively
    
    #   4.  The greatest increase in profits (date and amount) over the entire period
    #   5.  The greatest decrease in losses (date and amount) over the entire period
    #         need to use max/min command on a list? or dict?
    #         Using the list command i can find what entry no. that the max was at then use
    #         that to display
 

# HW Attempt: PyBank
# Import modules
import os
import csv

# Set the path
datapath = os.path.join('..','Resources', 'PyBank_Data.csv')

# Read the csv data
with open(datapath) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)

    # Create separate lists for the date and P/Ls field
    dates = []
    profits_losses = []
    for row in reader:
        dates.append((row[0]))
        profits_losses.append((row[1]))

    # 1. Number of entries
    no_months = len(dates)

    # 2. Loop to get the net profit from all entries
    net_profit = 0
    for x in profits_losses:
        int(x)
        net_profit += int(x)

    #3. Average Monthly Change
    monthly_change = []
    for i in range(len(profits_losses)):
        int(i)
        monthly_change[i] = row[1] -
    
    # length2 = len(monthly_change)
    # print(length2)
    # avg_profit = net_profit / no_months

    #4 & #5 Find the min and max profits
        # for x in profits_losses:
    #     if 

    # 6. Print the results and write to txt file
    print(f"Total # of Months: {str(no_months)}")
    print(f"Net Profit: ${str(net_profit)}")
    # print(f"Average Monthly Profit: ${str(avg_profit)}")
    # print(f"Total # of Months: {str(total_entries)}")
    # print(f"Total # of Months: {str(total_entries)}")
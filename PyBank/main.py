# PyBank Plan of Attack:
    # Resource data
    #   Col1: Date | MMM-YY | Min: 1/1/2010 | Max: 2/1/2017 |
    #   Col2: Profit/Losses | +/- # | Max: 1170593 | Min: -1196225 | 
    
    # Deliverables:
    #   1.  The total number of months included in the dataset
    #   2.  The net total amount of "Profit/Losses" over the entire period
    #   3.  The average of the changes in "Profit/Losses" over the entire period
    #   4.  The greatest increase in profits (date and amount) over the entire period
    #   5.  The greatest decrease in losses (date and amount) over the entire period
    #   6.  Write the results to a text file. 

 

# HW Attempt: PyBank
# Import modules
import os
import csv

# Set the path
datapath = os.path.join('..','Resources', 'PyBank_Data.csv')

# Read the csv data
with open(datapath) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    # Store header row
    headers = next(reader)

    # Create separate lists for the date and P/Ls field
    dates = []
    profits_losses = []

    for row in reader:
        dates.append((row[0]))
        profits_losses.append((row[1]))
    
    # Stores the P&L list as integers
    profits_losses = [int(i) for i in profits_losses]

# 1. Number of entries
    no_months = len(dates)

# 2. Loop to get the net profit from all entries
    net_profit = 0
    for x in profits_losses:
        net_profit += x

# 3. Average Monthly Change 
    # (referenced stackoverflow: https://stackoverflow.com/questions/2400840/finding-differences-between-elements-of-a-list)
    monthly_change = [j - i for i , j in zip(profits_losses[:-1],profits_losses[1:])]
    
    # Total # of changes
    num_changes = len(monthly_change)
    
    #loop for find the sum of all changes
    sum_change = 0
    for x in monthly_change:
        sum_change += x
    
    avg_change = (sum_change / num_changes)
    rd_avg = round(avg_change,2)

# 4. Find the max profit gain in a month 
    g_inc = max(profits_losses)
    index_g_inc = profits_losses.index(g_inc)
    date_g_inc = dates[index_g_inc]

# 5. Find the min and max profits
    g_dec = min(profits_losses)
    index_g_dec = profits_losses.index(g_dec)
    date_g_dec = dates[index_g_dec]

# 6. Print the results and write to txt file
    print("----------------------------")
    print("Financial Analysis:")
    print("")
    print(f"Total # of Months: {no_months}")
    print(f"Net Profit: ${net_profit}")
    print(f"Average Monthly Change: ${rd_avg}")
    print(f"Greatest Profit Increase: ${g_inc} in {date_g_inc}")
    print(f"Greatest Profit Decrease: ${g_dec} in {date_g_dec}")
    print ("----------------------------")

    resultspath = os.path.join('..','Analysis', 'Results_pybank.txt')
    with open(resultspath , "w") as text:
        text.write("----------------------------")
        text.write("\nFinancial Analysis:")
        text.write("\n")
        text.write(f"\nTotal # of Months: {no_months}")
        text.write(f"\nNet Profit: ${net_profit}")
        text.write(f"\nAverage Monthly Change: ${rd_avg}")
        text.write(f"\nGreatest Profit Increase: ${g_inc} in {date_g_inc}")
        text.write(f"\nGreatest Profit Decrease: ${g_dec} in {date_g_dec}")
        text.write ("\n----------------------------")
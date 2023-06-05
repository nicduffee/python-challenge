# Import modules
from pathlib import Path
import csv


# Print Title
print("\n")
print("Financial Analysis" + "\n")
print("----------------------------" + "\n")


# read in CSV file
csvpath = Path("Resources/budget_data.csv")

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Take out Headers row
    csv_header = next(csvreader)
    
    # set variables
    month_list = []
    profit_list =[]
    profit_total = 0
    profit_change = []


    # Loop through data
    for row in csvreader:
        # Append Date column to a list
        month_list.append(row[0])
        # Append Profit/Losses column to a list
        profit_list.append(row[1])
        

    # sum profits list to get total profit/losses
    for profit in profit_list:
        profit_total += int(profit)

    # Loop through profit/losses column to get each profit change
    for i in range(len(profit_list)-1):
        profit_change.append(int(profit_list[i+1]) - int(profit_list[i]))

    # Calculate average change
    profit_change_average = round(sum(profit_change) / len(profit_change), 2)

    #find greatest increase in profits
    max_increase = max(profit_change)
    max_index = profit_change.index(max_increase)
    max_month = month_list[max_index + 1]

    #find greatest decrease in profits
    min_increase = min(profit_change)
    min_index = profit_change.index(min_increase)
    min_month = month_list[min_index + 1]
    
    # Print results
    print(f"Total Months: {len(month_list)}" + "\n")
    print(f"Total: ${profit_total}" + "\n")
    print(f"Average Change: ${profit_change_average}" + "\n")
    print(f"Greatest Increase in Profits: {max_month} (${max_increase})" + "\n")
    print(f"Greatest Decrease in Profits: {min_month} (${min_increase})" + "\n")
    
# Write to file
output_path = Path("analysis/Budget_Analysis.txt")
with open(output_path, 'w') as file:
    file.write("\n")
    file.write("Financial Analysis" + "\n")
    file.write("----------------------------" + "\n")
    file.write(f"Total Months: {len(month_list)}" + "\n")
    file.write(f"Total: ${profit_total}" + "\n")
    file.write(f"Average Change: ${profit_change_average}" + "\n")
    file.write(f"Greatest Increase in Profits: {max_month} (${max_increase})" + "\n")
    file.write(f"Greatest Decrease in Profits: {min_month} (${min_increase})" + "\n")

    file.close







    




        






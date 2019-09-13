from pathlib import Path
import csv

csvpath=Path('../Resources/budget_data.csv')

total_months=0
total=0
average_change=0
greatest_increase_in_profits=0
greatest_decrease_in_profits=0

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        print(row)
        profit_loss=int(row[1])
        total=total+profit_loss
        total_months=total_months+1
        average_change=round(total/total_months,2)
        
        if greatest_decrease_in_profits==0:
            #profit_loss is the value of the first day
              greatest_increase_in_profits=profit_loss
            greatest_decrease_in_profits=profit_loss  
        elif profit_loss>greatest_increase_in_profits: 
            #Updating greatest increase today(profit_loss)
            greatest_increase_in_profits=profit_loss
        elif profit_loss<greatest_decrease_in_profits:
            greatest_decrease_in_profits=profit_loss
            
    print("```text\n")
print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: {total}\n")
print(f"Average Change: {average_change}\n")
print(f"Greatest Increase in Profits: {greatest_increase_in_profits}\n")
print(f"Greatest Decrease in Profits: {greatest_decrease_in_profits}\n")

output_path='output.txt'

with open (output_path,'w') as file:
    file.write("```text\n")
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: {total}\n")
    file.write(f"Average  Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_in_profits}\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_in_profits}\n")
   
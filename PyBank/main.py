from pathlib import Path
import csv
csvpath=Path('../Resources/budget_data.csv')
total=[]
line_num=0
with open (csvpath,'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
header.append('Total')
total.append(header)
line_num+=1
print(f"{header}")
for row in csvreader:
        total=int(row[1])
        total.append
        total=total+row[1]
        total_months=total_months+1
total_months=0
total=0
average_change=0
greatest_increase_in_profits=0
greatest_decrease_in_profits=0

for row in total:
    total=total+row[1]
    total_months=total_months+1
    average_change=total/total_months
if greatest_decrease_in_profits==0
    greatest_decrease_in_profits=total
elif total>greatest_increase_in_profits:
    greatest_increase_in_profits=total
elif total<greatest_decrease_in_profits:
    greatest_decrease_in_profits=total
    
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
   
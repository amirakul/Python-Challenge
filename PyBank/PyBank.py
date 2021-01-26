import os
import csv
#Connecting to the data
csvpath = os.path.join("Resources", "budget_data.csv")


#Initial variables
total_months=[]
total_revenue=[]
monthly_revenue_change=[]



#Open and read csv file
with open(csvpath) as csvfile:
   csvreader=csv.reader(csvfile, delimiter=",")
#Skip the header/1st row
   header = next(csvreader)
#Iterate through rows
   for row in csvreader:
       #Finding total months and revenue
       total_months.append(row[0])
       total_revenue.append(int(row[1]))

#Getting monthly change
   for i in range(len(total_revenue)-1):
       monthly_revenue_change.append(total_revenue[i+1]-total_revenue[i])

#Finding max and min revenue
greatest_increase_in_revenue=max(monthly_revenue_change)
greatest_decrease_in_revenue=min(monthly_revenue_change)


#Locating min and max months
greatest_increase_index = monthly_revenue_change.index(greatest_increase_in_revenue)+1
greatest_month = total_months[greatest_increase_index]
greatest_decrease_index = monthly_revenue_change.index(greatest_decrease_in_revenue)+1
worst_month = total_months[greatest_decrease_index]

# greatest_increase_in_revenue=monthly_revenue_change.index(min(monthly_revenue_change))+1


#Generate Paragraph Analysis Output
output = (
   f"Financial Analysis\n"
   f"_______________________\n"
   f"Total Months: {len(total_months)}\n"
   f"Total: {sum(total_revenue)}\n"
   f"Average Change: {sum(monthly_revenue_change)/len(monthly_revenue_change)}\n"
   f"Greatest Increase in Profits: {greatest_month} (${str(greatest_increase_in_revenue)})\n"
   f"Greatest Decrease in Profits: {worst_month} (${str(greatest_decrease_in_revenue)})\n"
)
#Print all the results in the terminal
print(output)

#Save the results to analysis text file
file_to_output = os.path.join("Analysis", "budget_analysis.txt")

with open(file_to_output, "w") as txt_file:
   txt_file.write(output)


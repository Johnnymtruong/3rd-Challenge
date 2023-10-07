import csv
import os

current_directory = os.getcwd()

# Specify the file name
file_name = "budget_data.csv"
folder_name = "Pybank"
subfolder_name = "Resources"
# Construct the full path to the CSV file
csv_file_path = os.path.join(current_directory, "Assignment_3", folder_name, subfolder_name, file_name)

# Create empty lists to store data from the CSV file
dates = []
profits_losses = []

# Open and read the CSV file
with open(csv_file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row if it exists
    header = next(csvreader, None)
    
    # Iterate through each row in the CSV file
    for row in csvreader:
        # Assuming "Date" is in the first column (index 0) and "Profit/Losses" in the second column (index 1)
        date = row[0]
        profit_loss = int(row[1])  # Convert the Profit/Losses value to an integer
        
        # Append the data to the respective lists
        dates.append(date)
        profits_losses.append(profit_loss)


# Changes in Profit/Losses
previous_profit_loss = 0
total_change = 0
num_changes = 0

        
greatest_increase = 0
greatest_decrease = 100000000

for i in range(len(profits_losses)):
  
    #greatest increase
    if (profits_losses[i] > previous_profit_loss):
        change_i = profits_losses[i] - previous_profit_loss
        total_change += change_i
        if (change_i > greatest_increase):
            greatest_increase = change_i
            m_i = dates[i]
        num_changes += 1
            
    
    #gretest decrease
    if (profits_losses[i] < previous_profit_loss):
        change_d = profits_losses[i] - previous_profit_loss
        total_change += change_d
        if (change_d < greatest_decrease):
            greatest_decrease = change_d
            m_d = dates[i]
        num_changes += 1
        
    previous_profit_loss = profits_losses[i]
    
avg_change = (total_change - profits_losses[0]) / (num_changes - 1)
print("Financial Analysis")
print("-"*30)
print("Total Months:", len(dates))
print("Total: $" + str(sum(profits_losses)))
print("Average Change: $" +str(round(avg_change,2)))
print("Greatest Increase in Profits: " + m_i +" ($" +str(greatest_increase)+")")
print("Greatest Decrease in Profits: " + m_d +" ($" +str(greatest_decrease)+")")

output_file = os.path.join("Analysis","financial_analysis.txt")
with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-" * 30 + "\n")
    txtfile.write(f"Total Months: {len(dates)}\n")
    txtfile.write(f"Total Profit/Loss: ${sum(profits_losses)}\n")
    txtfile.write(f"Average Change: ${avg_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {m_i} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {m_d} (${greatest_decrease})\n")
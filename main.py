import csv
import os

current_directory = os.getcwd()

# Specify the file name
file_name = "election_data.csv"
folder_name = "PyPoll"
subfolder_name = "Resources"

voter_ID = []
counties= []
candidates = []
# Construct the full path to the CSV file
csv_file_path = os.path.join(current_directory, "Assignment_3", folder_name, subfolder_name, file_name)
with open(csv_file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row if it exists
    header = next(csvreader, None)
    
    # Iterate through each row in the CSV file
    for row in csvreader:
        # Assuming "Date" is in the first column (index 0) and "Profit/Losses" in the second column (index 1)
        voter = row[0]
        county = row[1]  # Convert the Profit/Losses value to an integer
        candidate = row[2]
        # Append the data to the respective lists
        voter_ID.append(voter)
        counties.append(county)
        candidates.append(candidate)
        

dist_candidate = set(candidates)

vote_1 = 0
vote_2 = 0
vote_3 = 0


for i in range(len(voter_ID)):
    if (candidates[i] == "Charles Casper Stockham"):
        vote_1 += 1
    elif (candidates[i] == "Diana DeGette"):
        vote_2 += 1
    elif (candidates[i] == "Raymon Anthony Doane"):
        vote_3 += 1

    

per_1 = round((vote_1/len(voter_ID))*100,3)
per_2 = round((vote_2/len(voter_ID))*100,3)
per_3 = round((vote_3/len(voter_ID))*100,3)

print("Election Results")
print("-"*30)
print("Total Votes: " + str(len(voter_ID)))
print("-"*30)
print("Charles Casper Stockham: " +str(per_1) + "% ("+str(vote_1)+")")
print("Diana DeGette: " +str(per_2) + "% ("+str(vote_2)+")")
print("Raymon Anthony Doane: " +str(per_3) + "% ("+str(vote_3)+")")
print("-"*30)
print("Winner: Diana DeGette")
print("-"*30)

output_file = os.path.join("Analysis","election_results.txt")
with open(output_file, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-" * 30 + "\n")
    txtfile.write(f"Total Votes: {len(voter_ID)}\n")
    txtfile.write("-" * 30 + "\n")
    txtfile.write(f"Charles Casper Stockham: {per_1}% ({vote_1})\n")
    txtfile.write(f"Diana DeGette: {per_2}% ({vote_2})\n")
    txtfile.write(f"Raymon Anthony Doane: {per_3}% ({vote_3})\n")
    txtfile.write("-" * 30 + "\n")
    txtfile.write(f"Winner: Diana DeGette\n")
    txtfile.write("-" * 30 + "\n")
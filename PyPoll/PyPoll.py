import os
import csv

election_data_csv = os. path. join("..", "Resources", "election_data.csv")

#Initial variables
total_votes=[]
khan=[]
correy=[]
li=[]
otooley=[]

#Define a function
def print_percentages(election_data):
    khan= str(election_data[2])
    correy=str(election_data[2])
    li=str(election_data[2])
    otooley=str(election_data[2])




#Open and read csv file
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read the header row
    csv_header = next(csvfile)
    print(f"Header:{csv_header}")



    #Read each row after the header
    for row in csvreader:
        #Finding total votes
        total_votes.append(row[0])
        khan_percent= (int(khan)/total_votes)*100
        correy_percent= (int(correy)/total_votes)*100
        li_percent = (int(li)/total_votes)*100
        otooley_percent = (int(otooley)/total_votes)*100

        #Finding total votes for each candidate
        khan.append(row[2])
        correy.append(row[2])
        li.append(row[2])
        otooley.append(row[2])


        #Finding the winner
        winner = max(print_percentages)
        winner_name=str(winner)

#Generate output
output =(
    f"Election Results"
    f"________________________________"
    f"Total Votes : {len(total_votes)}"
    f"________________________________"
    f"Khan : {khan_percent}+ "%"+ "("+ {len(khan)} + ")""
    f"Correy : {correy_percent} + "%" + "(" + {len(correy)} +")"""
    f"Li : {li_percent} + "%" + "(" + {len(li)} +")""
    f"O'Tooley : {otooley_percent} + "%" + "(" + {len(otooley)} + ")""
    f"_____________________________________________"
    f"Winner : "+ {print(winner_name)}
    f"_____________________________________________"
)
print(output)


#Save the results to analysis as text file
file_to_output = os.path.join("Analysis", "poll_analysis.txt")
with open(file_to_output, "a") as txt_file:
   txt_file.write(output)







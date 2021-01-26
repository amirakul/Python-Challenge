import os
import csv


csvpath = os. path. join( "Resources", "election_data.csv")

#Initial variables
total_votes=0
total_candidates=0
winner_count=0
khancount=0
correycount=0
licount=0
otooleycount=0
winner_candidate=""





#Open and read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip the header row
    header = next(csvreader)


    #Iterate through rows
    for row in csvreader:
        #Finding total votes
        total_votes = total_votes + 1
        #Finding total votes for each candidates
        if (row[2]=="Khan"):
            khancount=khancount+1
        elif (row[2]=="Correy"):
            correycount=correycount+1
        elif (row[2]=="Li"):
            licount=licount+1
        elif (row[2]=="O'Tooley"):
            otooleycount=otooleycount+1
    #Calculating Percentages for each candidate:
    khanpercent=round(khancount/total_votes*100,2)
    correypercent=round(correycount/total_votes*100,2)
    lipercent=round(licount/total_votes*100,2)
    otooleypercent=round(otooleycount/total_votes*100,2)

    #Finding max votes for winner using if statements
    winner_count=max(khancount,correycount,licount,otooleycount)
    if winner_count==khancount:
        winner_candidate="Khan"
    elif winner_count==correycount:
        winner_candidate="Correy"
    elif winner_count==licount:
        winner_candidate="Li"
    else:
        winner_candidate="O'Tooley"




#Generate output
output = (
    f"Election Results\n"
    f"________________________________________\n"
    f"Total Votes : {total_votes}\n"
    f"___ ___ ___ ___ ___ ___ ___ ___ ___ ____\n"
    f"Khan : {khanpercent} %, ({khancount})\n"
    f"Correy : {correypercent} %, ({correycount})\n"
    f"Li : {lipercent} %, ({licount})\n"
    f"O'Tooley : {otooleypercent} %, ({otooleycount})\n"
    f"____ ____ _____ _____ _____ _____ _____ __\n"
    f"Winner : {winner_candidate}\n"
    f"____ ____ ____ _____ _____ _____ _____ ___n"
)
print(output)


#Save the results to analysis as text file
file_to_output = os.path.join("Analysis", "poll_analysis.txt")
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

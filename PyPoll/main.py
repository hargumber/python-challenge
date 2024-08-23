#import dependencies
import os
import csv

with open("analysis\pypoll_output.txt","w") as ofile:

    #Print header and demarcation line
    print("\n" + "Election Results" + "\n")
    ofile.write("\n" + "Election Results" + "\n\n")

    print("-------------------------------" + "\n")
    ofile.write("-------------------------------" + "\n\n")

    #open csv file
    csvpath = os.path.join("Resources", "election_data.csv")
    with open(csvpath,"r") as csvfile:

        #open the reader
        csv_reader = csv.reader(csvfile, delimiter = ",")

        #skip header
        header = next(csv_reader)

        #Total number of votes cast
        #Create empty lists for both votes and candidates
        votes = []
        candidates = []

        #create a list of votes(ballot id) and candidates
        for x in csv_reader:
            votes.append(x[0])
            candidates.append(x[2])

    #Calculate total votes cast
    votes_count = len(votes)

    #Output the result
    print("Total Votes: " + str(votes_count) + "\n")
    ofile.write("Total Votes: " + str(votes_count) + "\n\n")

    print("-------------------------------" + "\n")
    ofile.write("-------------------------------" + "\n\n")

    #Create a dictionary to hold candidates and their vote count
    candidate_count = dict()

    #Find the unique candidates and their vote counts
    for candidate in candidates:

        #If candidate is present in the dictionary then increase its previous count by 1 else add candidate with initial count as 1
        if candidate in candidate_count:
            candidate_count[candidate] += 1
        else:
            candidate_count[candidate] = 1

    #initiate variable for  winner and winning vote count.
    winner = ""
    winning_vote_count = 0

    #iterate over the candidate and their vote count dciotnary to find the candidate with max votes as well as percentage votes for each candidate
    for each_candidate in candidate_count:
        votes = candidate_count[each_candidate]
        if votes > winning_vote_count:
            winner = each_candidate
            winning_vote_count = votes

        #Calculate percentage vote for each candidate
        percentage = (votes/votes_count)*100

        #Round to 3 decimal places.
        percentage = round(percentage, 3)
        
        #Output the result
        print(each_candidate + ": " + str(percentage)+ "% " + str("(") + str(votes) + str(")") + "\n")
        ofile.write(each_candidate + ": " + str(percentage)+ "% " + str("(") + str(votes) + str(")") + "\n\n")

    #output line demarcation    
    print("-------------------------------" + "\n")
    ofile.write("-------------------------------" + "\n\n")

    #output winner details
    print("Winner : " + winner  + "\n")
    ofile.write("Winner : " + winner  + "\n\n")

    #output line demarcation    
    print("-------------------------------")
    ofile.write("-------------------------------\n")

    csvfile.close()
ofile.close()
  
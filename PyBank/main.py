#import dependencies
import os
import csv

#creating output file to save results to
with open("analysis\pybank_output.txt","w") as ofile:

    #Printing the header
    print("\n" + "Financial Analysis" + "\n")
    ofile.write("\n" + "Financial Analysis" + "\n\n")

    print("-------------------------------" + "\n")
    ofile.write("-------------------------------" + "\n\n")

    #set path for file
    csvpath = os.path.join("Resources", "budget_data.csv")
    #open the csv file
    with open(csvpath,"r") as csvfile:
        #Opening csv reader
        csv_reader = csv.reader(csvfile, delimiter =",")

        #skip header
        header = next(csv_reader)

        #convert profit_loss column into a list
        #Initiate empty lists
        profit_loss = []
        months = []

        #iterate over the rows and append a specific column data to the list
        #creating list of profit_loss and months separately
        for row in csv_reader:
            profit_loss.append(int(row[1]))
            months.append(row[0])

        #calculate the len of the list to find the total number of months
        months_count = len(profit_loss)

        #Output the result
        print("Total Months: " + str(months_count) + "\n")
        ofile.write("Total Months: " + str(months_count) + "\n\n")

        #Net amount of "Profit/Losses" over the entire period
        net_amount = sum(profit_loss)

        print("Total: $" + str(net_amount) + "\n")
        ofile.write("Total: $" + str(net_amount) + "\n\n")

        #the changes in "Profit/Losses" over the entire period
        #calculate differences between consecutive columns, (first value will be zero, do not include it in the calculations)
        #create an empty list to store differences
        changes = []

        #Iterate through profit/loss col starting from second element to gather difference for average change
        for i in range(1, len(profit_loss)):
            difference = (profit_loss[i]) - (profit_loss[i-1])
            changes.append(difference)

        #Calculate average of those changes
        average = sum(changes)/len(changes)
        average = round(average, 2)
        
        #Output the result
        print("Average Change: $" + str(average)+ "\n")
        ofile.write("Average Change: $" + str(average)+ "\n\n")

        #Find the greatest increase in the change i.e. max
        greatest_increase = max(changes)
        
        
        #Find the greatest decrease in the change i.e. min
        greatest_decrease = min(changes)

        #find index of greatest increase
        greatest_increase_month_index = changes.index(greatest_increase) + 1

        #find corresponding month for greatest increase
        greatest_increase_month = months[greatest_increase_month_index]

        #find index of greatest decrease
        greatest_decrease_month_index = changes.index(greatest_decrease) + 1

        #find corresponding month for greatest decrease        
        greatest_decrease_month = months[greatest_decrease_month_index]

        #Output the results
        print("Greatest Increase in Profits: " + str(greatest_increase_month) + str(" (") + str("$") + str(greatest_increase) + str(")") + "\n")
        ofile.write("Greatest Increase in Profits: " + str(greatest_increase_month) + str(" (") + str("$") + str(greatest_increase) + str(")") + "\n\n")
        print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + str(" (") + str("$") + str(greatest_decrease) + str(")") + "\n")
        ofile.write("Greatest Decrease in Profits: " + str(greatest_decrease_month) + str(" (") + str("$") + str(greatest_decrease) + str(")") + "\n")

    csvfile.close()
ofile.close()
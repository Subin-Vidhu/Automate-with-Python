import csv

#open the csv file
with open("C:/Users/Subin-PC/Downloads/CSV/new_train_aug14_2023.csv", newline="") as csvfile:
    #create a reader object
    reader = csv.reader(csvfile, delimiter=",")

    #loop through the rows in the csv file
    for row in reader:
        #print out the contents of each row
        print(row)


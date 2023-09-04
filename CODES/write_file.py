# Write
f = open("C:/Users/Subin-PC/Documents/automate-with-python.txt", "w")
f.write("This is my file!")
f.close()

# Write lines
f = open("C:/Users/Subin-PC/Documents/automate-with-python.txt", "w")
f.write('Line 1')
f.write('Line 2')
f.write('Line 3')
f.close()

# Write line by line from a list
f = open("C:/Users/Subin-PC/Documents/automate-with-python.txt", "w")
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
f.writelines(lines)
f.close()

# csv
import csv
 
my_list = [1, 2, 3, 4, 5]
with open('C:/Users/Subin-PC/Documents/automate-with-python-output.csv', 'w', newline='') as csvfile:
    mywriter = csv.writer(csvfile, delimiter=',')
    mywriter.writerow(my_list)
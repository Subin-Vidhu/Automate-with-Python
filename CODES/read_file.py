# Normal (read)
f = open('C:/Users/Subin-PC/Documents/Flask Local Host to aira_aramis_ai.txt','r')

data = f.read()

f.close()
print(data)

# readlines 
f = open('C:/Users/Subin-PC/Documents/Flask Local Host to aira_aramis_ai.txt','r')

lines = f.readlines()

for line in lines:
    print(line)
f.close()

# readline
f = open('C:/Users/Subin-PC/Documents/Flask Local Host to aira_aramis_ai.txt','r')
line = f.readline()

while line:
    print(line)
    line = f.readline()

f.close()

# path
import os.path

filename = "C:/Users/Subin-PC/Documents/Flask Local Host to aira_aramis_ai.txt"

if os.path.isfile(filename):
    with open(filename, "r") as f:
        contents = f.read()
        print(contents)
else:
    print("File does not exist.")


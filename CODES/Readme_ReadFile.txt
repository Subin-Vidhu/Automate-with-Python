Read File (notes)
We're going to learn about files with Python.



Python can read a variety of file types, including text files (.txt), comma-separated values (.csv), web pages (.html/.htm), JavaScript Object Notation (.json), Extensible Markup Language (.xml).

It can also read data from databases such as SQLite, MySQL, and Oracle. Python can also work with image and audio files, but those are not text-based so we'll not cover those in this video.

Read File
We'll take a look at reading text files with Python now.

Reading files is a very common task in Python. In order to read a file, we first need to open it. We do this with the open() function.

open() takes two arguments: the path to the file, and the mode. Mode is optional, but it specifies how the file should be opened. The most common mode is 'r', which stands for read.

f = open("example.txt", "r")
Once the file is open, we can use the read() method to read its contents.

data = f.read()
read() takes an optional argument, which is the number of characters to read. If we don't specify a number, it will read the entire file.

Finally, we need to close the file with the close() method.

We'll read it and print it to the screen.

f.close()
print(data)
As you can see, it's pretty simple to read files with Python.

Read File Line by Line
Now you will learn how to read a file line by line in Python. We'll read a file called test.txt which has some text in it.

We can then open this file in Python using the open() function:

f = open("test.txt", "r")
Once the file is open, we can use the readlines() function to read all of the lines into a list:

lines = f.readlines()
We can then iterate over this list to print each line:

for line in lines:
    print(line)
We can also use the readline() function to read a single line at a time:

line = f.readline()
 
while line:
    print(line)
    line = f.readline()
Finally, don't forget to close the file when you're done:

f.close()
File Exists?
In Python, you can use the os.path module to check if a certain file exists. For example, let's say you have a file called test.txt in the current directory. You can check if this file exists using the following code:

import os.path
 
if os.path.isfile("test.txt"):
    print("File exists!")
else:
    print("File does not exist.")
Read File into List
Now let's take a look at reading a file into a Python list.

Reading a file into a list is a two step process.

First, you need to open the file using the open() function. This will return a file object.

Second, you can use the file object's readlines() method to read the file one line at a time and add each line to a list.

Here's a quick example:

f = open("myfile.txt")
mylist = f.readlines()
f.close()
Here's an example of checking if a file exists and reading the file in Python.

You can use the os.path module to check if a file exists and then read it.

import os.path
 
filename = "myfile.txt"
 
if os.path.isfile(filename):
    with open(filename, "r") as f:
        contents = f.read()
        print(contents)
    else:
        print("File does not exist.")
When running the program, it checks if the file exists before reading it.

CSV files?
A CSV (comma-separated values) file is a type of plain text file that stores tabular data. It is commonly used for exporting and importing data between different programs or databases. A CSV file consists of a series of values separated by commas, with each row representing a record.



CSV files can be opened and edited in any text editor, such as Notepad. But they can also be opened in Microsoft Excel or Google Sheets,

where the data shows up in the different cells of  the spreadsheet.

If you want to create a CSV file, you can use Microsoft Excel or Google Sheets and export as CSV file. You can also create them in notepad or any text-based editor.

The data in the file could look something like this:

Name,Age,City
John Doe,25,New York
Jane Doe,30,Los Angeles
Bob Smith,45,Chicago
But there is no limit on the number of cells and rows you add to it.  It is possible to read csv files without any modules, using the code you have used before. But using modules saves you a lot of time when programming. You can think if modules as building blocks. There's a Python module called csv, which as you might have guessed, is for reading csv files.

#import the csv module
import csv
 
#open the csv file
with open("data.csv", newline="") as csvfile:
    #create a reader object
    reader = csv.reader(csvfile, delimiter=",")
    
    #loop through the rows in the csv file
    for row in reader:
        #print out the contents of each row
        print(row)
If you run this program, you should have the file data.csv in the same directory as your program. It will show the contents of the csv file.

JSON data
Next we will look at JSON.

JSON is like a secret code. It's a way of writing down information so that computers can understand it. It's like a special language that only computers can read.

A file with JSON data contains something like this:

[
  {
    "id": 1,
    "name": "John Doe",
    "age": 28,
    "hobbies": [
      "running",
      "reading",
      "swimming"
    ]
  },
  {
    "id": 2,
    "name": "Jane Doe",
    "age": 24,
    "hobbies": [
      "cooking",
      "painting",
      "dancing"
    ]
  }
]
Which both humans and computers can read, but it does look a bit cryptic. JSON can be read not only by Python program, but by almost all programming languages and is widely used throughout the web.

The following code snippet will read a JSON file and print its contents:

import json
 
# open and read the JSON file
with open("data.json", "r") as f:
    data = json.load(f)
 
# print the contents of the file
print(data)
And those are just some of the file types you can read with Python!
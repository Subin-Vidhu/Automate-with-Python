SQLite Database (notes)
I'm going to show you how to use an SQLite database with Python.

SQLite is a database that stores data in a file on your computer. Python is a programming language that lets you work with data in SQLite databases.

SQL is a computer language that helps you store, find, and change information in databases. Databases are like really big lists. They have lots of information in them, and you can use SQL to find and change that information.

For example, let's say you have a database of students. The database has a list of all the students in the school, their grades, and their addresses. You can use SQL to find all the students who live in a certain town, or all the students who got an A in math.

SQL is a really powerful tool, and it's used by lots of businesses and organizations to manage their data.

Example
We'll be using the sqlite3 module, which comes packaged with Python. If you don't have it installed, you can get it from the Python Package Index.

To use SQLite with Python, you need to import the sqlite3 module. You can do this at the top of your Python code:

import sqlite3
Once you've imported the sqlite3 module, you can connect to a database by creating a Connection object. To do this, you need to specify the database file name:

conn = sqlite3.connect('database.db')
Once you have a Connection object, you can create a Cursor object. This object lets you execute SQL commands on the database:

cursor = conn.cursor()
Now you're ready to start working with the database. For example, you can create a new table with the following SQL command:

cursor.execute('CREATE TABLE students (name text, age integer)')
You can insert data into the table with the following SQL command:

cursor.execute('INSERT INTO students (name, age) VALUES (?, ?)', ('Jesse', 13))
You can query the table to get data out of it. For example, the following SQL command will get all of the rows from the table:

cursor.execute('SELECT * FROM students')
You can also query the table to get specific rows. For example, the following SQL command will get all of the rows where the name is Jesse:

cursor.execute('SELECT * FROM students WHERE name = ?', ('Jesse',))
Once you're done working with the database, you need to close the connection:

conn.close()
That's a basic example of SQLite with Python.



Another example
Let's do another example of SQLite database with Python.

we can create a new database like this:

import sqlite3
 
conn = sqlite3.connect('example.db')
This will create a new file called example.db in your current directory.

Now that we have a connection to our database, we can create a table. For our user table, we'll need columns for the user's id, name, and email address. We can create the table with the following SQL:

conn.execute('''
CREATE TABLE users (
id INTEGER PRIMARY KEY,
name TEXT,
email TEXT
);
''')
Now that our table is created, we can insert some data into it. For our first user, we'll use an id of 1, a name of John Doe, and an email address of john@example.com. We can insert this data with the following SQL:

conn.execute('''
INSERT INTO users (id, name, email)
VALUES (1, 'John Doe', 'john@example.com');
''')
We can insert more data into our table in the same way. Let's add a second user with an id of 2, a name of Jane Smith, and an email address of jane@example.com.

conn.execute('''
INSERT INTO users (id, name, email)
VALUES (2, 'Jane Smith', 'jane@example.com');
''')
Now that we have some data in our table, we can query it. For example, we can get all of the users from our table like this:

conn.execute('''
SELECT * FROM users;
''')
This will return a list of tuples, with each tuple representing a row in our table.

We can also query for specific data. For example, if we only want the name and email address of our users, we can use the following SQL:

conn.execute('''
SELECT name, email FROM users;
''')
This will return a list of tuples, with each tuple containing the name and email address of a user.



We can also use WHERE clauses to filter our results. For example, if we only want to get the user with an id of 1, we can use the following SQL:

conn.execute('''
SELECT * FROM users
WHERE id = 1;
''')
This will return a list with a single tuple, containing the data for the user with an id of 1.

We can also use ORDER BY to sort our results. For example, if we want to get all of the users from our table, sorted by their name, we can use the following SQL:

conn.execute('''
SELECT * FROM users
ORDER BY name;
''')
This will return a list of tuples, with each tuple representing a row in our table. The tuples will be sorted by the name column in ascending order.



We can also use LIMIT to limit the number of results we get back. For example, if we only want to get the first two users from our table, we can use the following SQL:

conn.execute('''
SELECT * FROM users
LIMIT 2;
''')
This will return a list with two tuples, containing the data for the first two users in our table.
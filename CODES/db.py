import sqlite3

# create database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# create table
cursor.execute('CREATE TABLE students (name text, age integer)')

# add data
cursor.execute('INSERT INTO students (name, age) VALUES (?, ?)', ('Jesse', 13))

# fetch all table
res = cursor.execute('SELECT * FROM students')
print(res.fetchall())

# fetch one
res = cursor.execute('SELECT * FROM students WHERE name = ?', ('Jesse',))
print(res.fetchone())

# close database 
conn.close()


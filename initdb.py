import sqlite3

connection = sqlite3.connect('database.db')
print ('Opened database successfully')

connection.execute('CREATE TABLE films (name TEXT, rating TEXT, genre TEXT)')
print ('Table created successfully')

connection.close()

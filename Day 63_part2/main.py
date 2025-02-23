import sqlite3

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()

# creating table in database
cursor.execute("CREATE TABLE books (id INTERGER PRIMARY KEY, title varchar(200) NOT NULL UNIQUE, author varchar(200) NOT NULL, ratin FLOAT NOT NULL)")

#adding data to the database
cursor.execute("INSERT INTO books VALUES(1, 'Python for newbies', 'Emma', '10/10')")
db.commit() 
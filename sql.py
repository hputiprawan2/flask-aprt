import sqlite3

with sqlite3.connect("sample.db") as connection:
	# create a cursor
	c = connection.cursor()
	
	# drop table if exist
	# c.execute("""DROP TABLE posts""")

	# creation a new table
	c.execute("""CREATE TABLE posts(title TEXT, description TEXT)""")
	c.execute('INSERT INTO posts VALUES("Good", "This is good.")')
	c.execute('INSERT INTO posts VALUES("Nice", "This is nice.")')
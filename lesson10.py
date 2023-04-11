import sqlite3

connection  = sqlite3.connect('itstep.sl3', 5)
cur = connection.cursor
cur.execute("CREATE TABLE first_table (name date_temp);")
cur.commit
connection.close
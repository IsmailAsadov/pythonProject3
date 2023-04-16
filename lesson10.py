import sqlite3

connection  = sqlite3.connect('itstep.sl3', 5)
cur = connection.cursor
cur.execute("CREATE TABLE first_table (name);")
cur.commit
cur.execute("insert into first_table values(John)")
cur.commit
cur.execute("insert into first_table values(Kate)")
cur.commit
cur.execute("select in first_table rowid = 2")
cur.commit
cur.execute("update set name = Katherine where rowid = 2, ")
cur.commit
cur.execute("select in first_table rowid = 1")
cur.commit
cur.execute("delete from first_table where rowid = 1")
cur.commit
cur.execute('drop table first_table')
cur.commit
connection.close
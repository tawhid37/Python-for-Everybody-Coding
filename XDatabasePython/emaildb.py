import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')

cur.execute('''
CREATE TABLE Ages (name TEXT, age INTEGER)''')

cur.execute('DELETE FROM Ages;')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Leechan", 38);')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Rahman", 40);')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Elouise", 38);')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Melice", 37);')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Etienne", 36);')

conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT hex(name || age) AS X FROM Ages ORDER BY X'

for row in cur.execute(sqlstr):
    print(str(row[0]))

cur.close()

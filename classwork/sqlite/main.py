import sqlite3

conn = sqlite3.connect('users.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name TEXT, age INTEGER)')

cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)' , ('Lilias', 39));
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)' , ('Jock', 21));
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)' , ('Corrin', 17));
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)' , ('Leaya', 19));
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)' , ('Francesco', 40))
cur.execute('INSERT INTO Ages (name, age) VALUES (?,?)' , ('Meabh', 39));


cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')

conn.commit()
for row in cur:
	print(row)
	break

cur.close()
conn.close()

# Code: http://www.pythonlearn.com/code3/db1.py
# Or select Download from this trinket's left-hand menu
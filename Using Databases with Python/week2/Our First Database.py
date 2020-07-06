#this assignment creates a new Database file and add data to added table
#then select first raw after convert it's content to hex


import sqlite3

#connect to sqlite and create a new file
connection = sqlite3.connect('first')
cur= con.cursor()

#delete existing data then create new one
cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('''CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
)''')

#  inserts many records at a time
insertV = [('Maisey', 39),
             ('Luk', 17),
             ('Marco', 36),
            ('Zakaria', 36),]
cur.executemany('INSERT INTO Ages VALUES (?,?)', insertV)

connection.commit()

#select first raw after converting it's content into hex
sqlstr ='SELECT hex(name || age) AS X FROM Ages ORDER BY X'
for raw in cur.execute(sqlstr):
    print(raw)
    break

cur.close()


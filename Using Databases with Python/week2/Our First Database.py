#----------------------------------------------------------------------
#In this assignment I use python3 to create a new Database file 
#Add a table (Ages)
#Insert data to DB table using python code
#select first raw after convertinhg it's content to ordered hexadecimal 
#----------------------------------------------------------------------
import sqlite3

#connect to sqlite and create a new file
connection = sqlite3.connect('first')
cur= con.cursor()

#delete existing data then create a new one
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


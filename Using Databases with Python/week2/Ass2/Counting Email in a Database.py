import sqlite3

#connect to sqlite and create a new file
con = sqlite3.connect('emaildb.sqlite')
cur= con.cursor()

#delete existing data then create new one
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

#read data from text file
fileName= input('Enter file name: ')
if len(fileName)< 1 : fileName='mbox.txt'
fileData = open(fileName)

#Get e-mails by searching for lines starting with from
for line in fileData:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    #find each mail organization
    parts = email.split('@')
    org = parts[-1]
    #--to test--
    # print (org)

    #add data to DB if not exist
    #increment if exist
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
        
# This statement commits outstanding changes to disk each
# time through the loop - the program can be made faster
# by moving the commit so it runs only after the loop completes
con.commit()

#print the count of e-mails of each organization (top 10)
#https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

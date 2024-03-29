  
#----------------------------------------------------------------------
#In this assignment I use python3 to create a new Database file 
#Add a many tables 
#Insert data to DB tables from a json file
#connect tables with additional table (many to many relation)
#get new table by using (join) on many tables 
#----------------------------------------------------------------------
import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# DB setup drop then add 
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

#read datafrom json file
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

#extract data from each line in the file
for entry in json_data:

    name = entry[0];
    title = entry[1];
    role = entry[2];
    
    #check
    #print((name, title,role))

    #fill DB with json data 
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id,role) VALUES ( ?, ? ,? )''',
        ( user_id, course_id,role ) )

    #save data in DB sqlite
    conn.commit()
  
# print first row
sqlstr = 'SELECT hex(User.name || Course.title || Member.role ) AS X FROM User JOIN Member JOIN Course ON User.id = Member.user_id AND Member.course_id = Course.id ORDER BY X'
for row in cur.execute(sqlstr) :
    print (row)
    break

#close connection
cur.close()

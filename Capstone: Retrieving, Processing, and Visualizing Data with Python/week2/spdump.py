import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

#Consider inbound like Download and outbound like Upload.
#If your server requests data from an external source it will DOWNLOAD that data into the server. [INBOUND TRANSFER]
#If some user requested a webpage, the server will upload that page to the client side. [OUTBOUND TRANSFER]
#as inbound?
#You have it correct. Data "inbound" to Amazon (that is, packet data that is destined for the Amazon cloud servers; for example, uploads and client requests) are free. Data "outbound" from Amazon is billed (that is, downloads from the cloud and responses to client requests).
cur.execute('''SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url
     FROM Pages JOIN Links ON Pages.id = Links.to_id
     WHERE html IS NOT NULL
     GROUP BY id ORDER BY inbound DESC''')

count = 0
for row in cur :
    if count < 50 : print(row)
    count = count + 1
print(count, 'rows.')
cur.close()

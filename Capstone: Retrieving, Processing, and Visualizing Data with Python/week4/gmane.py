import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
import sqlite3
import ssl
import re
#https://docs.python.org/3/library/time.html
import time
from datetime import datetime, timedelta

# Not all systems have this so conditionally define parser
try:
    # https://dateutil.readthedocs.io/en/stable/index.html#
    import dateutil.parser as parser
except:
    # placeholder to avoid getting an error when empty code is not allowed.
    # note: Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
    pass

#---------------------------------------------
#function: parsemaildate
# try to parse emails with dateutil
#if not exist
#---------------------------------------------
def parsemaildate(md) :
    # See if we have dateutil
    try:
        # https://dateutil.readthedocs.io/en/stable/parser.html
        # parser.parse(parserinfo=None, **kwargs)
        # Parse a string in one of supported formats, using parserinfo parameters.
        # Returns a datetime.datetime object or
        pdate = parser.parse(tdate)###tdate
        #https://www.geeksforgeeks.org/python-pandas-timestamp-isoformat/
        #isoformat() to convert the given Timestamp object into the ISO format
        test_at = pdate.isoformat()
        return test_at
    except:
        pass

    # Non-dateutil version - we try our best

    # Try a bunch of format variations - strptime(string,format) is *lame*
    # method creates a datetime object from the given string(certain format).
    #https://www.programiz.com/python-programming/datetime/strptime
    dnotz = None
    pieces = md.split()
    # join function: to join list
    notz = " ".join(pieces[:4]).strip()
    #https://devhints.io/datetime
    #all kinds of date and time[:4]
    for form in [ '%d %b %Y %H:%M:%S', '%d %b %Y %H:%M:%S',
        '%d %b %Y %H:%M', '%d %b %Y %H:%M', '%d %b %y %H:%M:%S',
        '%d %b %y %H:%M:%S', '%d %b %y %H:%M', '%d %b %y %H:%M' ] :
        try:
            dnotz = datetime.strptime(notz, form)
            break
        except:
            #note: difference between continue and pass
            #continue will jump back to the top of the loop.
            #pass will continue processing.
            continue

    if dnotz is None :
        # print 'Bad Date:',md
        return None

    iso = dnotz.isoformat()

    ###
    tz = "+0000"
    try:
        tz = pieces[4]
        ival = int(tz) # Only want numeric timezone values
        if tz == '-0000' : tz = '+0000'
        tzh = tz[:3]
        tzm = tz[3:]
        tz = tzh+":"+tzm
    except:
        pass

    return iso+tz
#---------------------------------------------

# Ignore SSL certificate errors
#https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()

baseurl = "http://mbox.dr-chuck.net/sakai.devel/"

cur.execute('''CREATE TABLE IF NOT EXISTS Messages
    (id INTEGER UNIQUE, email TEXT, sent_at TEXT,
     subject TEXT, headers TEXT, body TEXT)''')

# RESTABLE PROCESS: Pick up where we left off ("max")
start = None
cur.execute('SELECT max(id) FROM Messages' )
try:
    row = cur.fetchone()
    #none: first time
    if row is None :
        start = 0
    else:
        start = row[0]
except:
    start = 0

#start = row[0]
if start is None : start = 0

many = 0
count = 0
fail = 0
while True:
    if ( many < 1 ) :
        #commit in loop because of failure condition
        conn.commit()
        sval = input('How many messages:')
        if ( len(sval) < 1 ) : break
        many = int(sval)

    #start = 0 or max(id)
    start = start + 1
    cur.execute('SELECT id FROM Messages WHERE id=?', (start,) )
    try:
        row = cur.fetchone()
        #already retrieved
        if row is not None : continue
    except:
        row = None

    many = many - 1

    #build url to retrieve specific message
    #baseurl = "http://mbox.dr-chuck.net/sakai.devel/101/102"
    url = baseurl + str(start) + '/' + str(start + 1)

    text = "None"
    try:
        #https://docs.python.org/3/library/urllib.request.html
        #(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
        # CA certificates for HTTPS requests
        document = urllib.request.urlopen(url, None, 30, context=ctx)
        text = document.read().decode()

        # check 3 types of errors
        if document.getcode() != 200 :
            print("Error code=",document.getcode(), url)
            break

    except KeyboardInterrupt:
        print('')
        print('Program interrupted by user...')
        break

    except Exception as e:
        print("Unable to retrieve or parse page",url)
        print("Error",e)
        # failure condition(Unretrievable/no from/no \n\n )
        fail = fail + 1
        if fail > 5 : break
        continue

    print(url,len(text))
    count = count + 1

    # all starts with from or it could be bad data
    if not text.startswith("From "):
        print(text)
        print("Did not find From ")
        fail = fail + 1
        if fail > 5 : break
        continue

    # our mail data: headers then 2 lines then body
    pos = text.find("\n\n")
    if pos > 0 :
        hdr = text[:pos]
        body = text[pos+2:]
    else:
        print(text)
        print("Could not find break between headers and body")
        fail = fail + 1
        if fail > 5 : break
        continue

    email = None
    #egular expression (\S+ one or more non-blank characters)
    x = re.findall('\nFrom: .* <(\S+@\S+)>\n', hdr)
    if len(x) == 1 :
        email = x[0];
        email = email.strip().lower()
        email = email.replace("<","")
    else:
        x = re.findall('\nFrom: (\S+@\S+)\n', hdr)
        if len(x) == 1 :
            email = x[0];
            email = email.strip().lower()
            email = email.replace("<","")

    date = None
    #date, blank, any numbers of characters, comma
    #Date: Wed, 14 Dec 2005 16:41"01 -500
    y = re.findall('\Date: .*, (.*)\n', hdr)
    if len(y) == 1 :
        tdate = y[0]
        tdate = tdate[:26]
        try:
            sent_at = parsemaildate(tdate)
        except:
            print(text)
            print("Parse fail",tdate)
            fail = fail + 1
            if fail > 5 : break
            continue

    subject = None
    z = re.findall('\Subject: (.*)\n', hdr)
    if len(z) == 1 : subject = z[0].strip().lower();

    # Reset the fail counter
    fail = 0
    print("   ",email,sent_at,subject)
    cur.execute('''INSERT OR IGNORE INTO Messages (id, email, sent_at, subject, headers, body)
        VALUES ( ?, ?, ?, ?, ?, ? )''', ( start, email, sent_at, subject, hdr, body))
    if count % 50 == 0 : conn.commit()
    if count % 100 == 0 : time.sleep(1)

conn.commit()
cur.close()

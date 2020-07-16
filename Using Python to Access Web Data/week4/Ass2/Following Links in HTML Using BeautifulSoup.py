'''
In this assignment you will write a Python program that expands on 
https://www.py4e.com/code3/urllinks.py
The program will use urllib to read the HTML from the data files below, 
extract the href= values from the anchor tags, 
scan for a tag that is in a particular position from the top and follow that link,
repeat the process a number of times, and report the last name you find.
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter Url: ')
count = int(input("Enter count: "))
position = int(input("Enter position:"))
for i in range(count):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)

    print (s[position-1])
    print (t[position-1])
    url = s[position-1]


  '''
In this assignment you will write a Python program
similar to http://www.pythonlearn.com/code/urllink2.py.
The program will use urllib to read the HTML from the data files below,
and parse the data, extracting numbers and compute the
sum of the numbers in the file.
data: http://python-data.dr-chuck.net/comments_353539.html (Sum ends with 63)
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
#Assignment1
sum =0
tags = soup('span')
for tag in tags:
    # print(tag) <span class="comments">1</span>
    sum = sum + int(tag.contents[0])
    #Or# sum = sum + int(tag.text)
print(sum) 

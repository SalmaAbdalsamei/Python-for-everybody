'''
In this assignment you will write a Python program that will prompt for a URL, 
read the XML data from that URL using urllib and then parse and
extract the comment counts from the XML data, 
compute the sum of the numbers in the file and
enter the sum,
'''
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url: ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)
results = tree.findall('comments/comment')

count =0
sum=0

for item in results:
    x = int(item.find('count').text)
    count =count+1
    sum = sum+x
    
print(sum)

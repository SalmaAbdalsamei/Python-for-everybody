'''
The program will prompt for a URL, 
read the JSON data from that URL using urllib and then 
parse and extract the comment counts from the JSON data, 
compute the sum of the numbers in the file.
'''
from urllib.request import urlopen
import json

url = input("Enter url")
html = urlopen(url).read()
info = json.loads(html)
print('User count:', len(info))

count=0
sum=0

for item in info['comments']:
    count = count + 1
    sum = sum+item['count']
    
print(sum)


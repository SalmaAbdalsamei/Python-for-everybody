'''
Write a program to read through the mbox-short.txt 
figure out the distribution by hour of the day for each of the messages. 
Once you have accumulated the counts for each hour, 
print out the counts, sorted by hour.
'''
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dic = dict()

for line in handle:
    #From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    if not line.startswith("From "): continue
    
    p = line.split('From ')
    word = p[1].split()
    Time = word[4]
    hr=(Time.split(':'))[0]
    
    if hr  in dic.keys():
        dic[hr]=dic.get(hr,0)+1
        
    if hr not in dic.keys():
        dic[hr]=1
        
lst = (sorted([(k,v) for k,v in dic.items()]))

for k,v in lst:
    print(k,v)
    

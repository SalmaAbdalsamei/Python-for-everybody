'''
Write a program to read through the mbox-short.txt and
figure out who has sent the greatest number of mail messages. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
then finds the most prolific committer.
'''
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dic = dict()
Val =1

for line in handle:
    if not line.startswith("From "): continue
    p = line.split('From ')
    word = p[1].split()
    email = word[0]
    
    if email  in dic.keys():
        dic[email]=dic.get(email,0)+1
        
    if email not in dic.keys():
        dic[email]=1
        
for key in dic.keys():
    if Val < dic[key]:
        Val = dic[key]
        k = key
        
print(k,Val)

'''
Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words. 
The program should build a list of words. 
For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.
data at http://www.py4e.com/code3/romeo.txt
'''
fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    splt= line.split()
    for word in splt:
        if not word in lst:
           lst.append(word)
           
lst.sort()     
print(lst)

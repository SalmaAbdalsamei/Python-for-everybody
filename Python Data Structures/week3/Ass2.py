'''
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and 
extract the floating point values from each of the lines and 
compute the average of those values.
data at http://www.py4e.com/code3/mbox-short.txt 
'''
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
all = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    i = line.split(':')
    s= i[1]
    all+= float(s)
    count= count+1
print('Average spam confidence:',all/count)

'''
Write a program that prompts for a file name, and print the contents of the file in upper case. 
Use the file words.txt to produce the output below.
http://www.py4e.com/code3/words.txt
'''
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for word in fh : 
    wordnew = word.rstrip()
    print(wordnew.upper())

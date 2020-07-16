#----------------------------------------------------------------------
#In this assignment you will read through and parse a file with text and numbers.
#You will extractall the numbers in the file and compute the sum of the numbers.
#data: http://py4e-data.dr-chuck.net/regex_sum_739468.txt (There are 94 values and the sum ends with 484)
#------------------------------------------------------------------
import re

fname = raw_input('Enter File name :')
handle = open(fname)

sum=0
count = 0

for line in handle:	
  #[0-9]:any number
	N = re.findall('[0-9]+',line)
	
	for num in N:		
		if num >= [0]:			
			count = count + 1
			sum = sum + int(num)
		
print ('Count =',count,'sum =',sum)

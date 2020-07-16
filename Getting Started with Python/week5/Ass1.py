'''
Write a program to prompt the user for hours and rate per hour 
using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
'''
hrs = input("Enter Hours:")
rate= input ("Enter hourly rate")

h = float(hrs)
r =float(rate)

if hrs <= 40.0 :
    pay=h*r
    print(pay)
else :
    pay =(40*r)+((h-40)*r*1.5)
    print(pay)

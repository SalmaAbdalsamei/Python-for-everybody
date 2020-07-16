'''
Write a program to prompt the user for hours and rate per hour 
using input to compute gross pay. 
Do not worry about error checking or bad user data.
'''
hrs = input("Enter Hours:")
rate= input ("Enter Rate per hour")

grosspay = float(hrs) * float( rate)
print("Pay:",grosspay)

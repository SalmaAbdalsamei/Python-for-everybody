'''
Write a program to prompt for a score between 0.0 and 1.0. 
If the score is out of range, print an error. 
If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit.
'''
score = input("Enter Score: ")

try:
    f=float(score)
except:
    print("error")
    
if f>=0.0 and f <= 1.0:
    if f>=0.9:
        print('A')
    elif f>=0.8:
        print('B')
    elif f>=0.7:
        print('C')
    elif f>0.6:
        print('D')
    elif f<0.6:
        print('F')
else:
    print("error")
    exit()
    

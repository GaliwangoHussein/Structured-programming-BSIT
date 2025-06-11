## if statements

'''
syntax

if condition:
    logic
elif condition:
    logic
 else:      
    logic

 '''           

## Aprogram that accepts a number from the user (1-9)
# it tells him the number entered

print("Welcome to Number Teller")
number = int(input("please eneter a number between 1 and 9 "))
if number ==1:
    print("you have entered number one")
elif number == 2:
    print("you have entered number two")
elif number == 3:
    print("you have number three")
elif number == 4:
    print("you have number four")
elif number == 5:
    print("you have number five")
elif number == 6:
    print("you have number six")
elif number == 7:
    print("you have number seven")
elif number == 8:
    print("you have number eight")
elif number == 9:
    print("you have number nine")
else:
    print("Invalid, please enter a number between 1 and 9")

#TODO
'''
With the use of if statements, write a python program that allows an
instructor to enter a mark betwwen 0 and 100.

on receiving the mark, the program has to assign a grade based on your
defined clusters ie 80-90 is A, 91-100 is A+ etc.
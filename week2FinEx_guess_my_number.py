#!/usr/bin/python
#In this problem, you'll create a program that guesses a secret number!
#The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!```
#
high=10
low=0
iteration=0

print("Please think of a secret number between 0 and 10")

while True:
    iteration+=1
    mid=(high+low)/2
    
    c=input("is your number " + str(mid) + " ? if yes hit y, if lower hit l, if higher hit y")
    
    if(c=='y'):
        print("You guessed",mid)
        break
    elif(c=='l'):
        low=mid
    elif(c=='h'):
        high=mid
print("The number of iterations it took to guess the secret number",iteration)

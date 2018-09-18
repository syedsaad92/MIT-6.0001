#!/usr/bin/python
#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

# Paste your code into this box 
#s = 'uxqsgwweeafredys'
count = 0
vowels = ['a','e','i','o','u']
for char in s:
    if char in vowels:
        count+=1
print ("Number of vowels:",count)

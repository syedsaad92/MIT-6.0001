Problem 4
15.0/15.0 points (graded)
Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters. For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]

This function takes in a list of strings and returns a list of strings. Your function should not modify aList.

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    
Code Editor

# Paste your function here
def lessThan4(aList):
    temp = []
    for char in aList:
        if (len(char)<4):
            temp.append(char)
    return temp

Press ESC then TAB or click outside of the code editor to exit
correctCorrect

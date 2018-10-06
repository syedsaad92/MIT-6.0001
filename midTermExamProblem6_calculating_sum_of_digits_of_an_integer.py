Problem 6
20.0/20.0 points (graded)
Write a recursive Python function, given a non-negative integer N, to calculate and return the sum of its digits.

Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while doing integer division by 10 removes the rightmost digit (126 // 10 is 12).

This function has to be recursive; you may not use loops!

This function takes in one integer and returns one integer.

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Your code here

# Paste your function here
def sumDigits(N):
    if N < 10:
        return N
    else:
        remainder = N % 10
        return remainder + sumDigits(N//10)

Correct
Test results
CORRECT

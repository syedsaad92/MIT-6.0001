Problem 3
10.0/10.0 points (graded)
Write a recursive Python function, given a non-negative integer N, to count and return the number of occurrences of the digit 7 in N.

For example:
count7(717) -> 2
count7(1237123) -> 1
count7(8989) -> 0
Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while doing integer division by 10 removes the rightmost digit (126 / 10 is 12).

This function has to be recursive; you may not use loops! This function takes in one integer and returns one integer.

def count7(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    
Code Editor

1
def count7(N):
2
    '''
3
    N: a non-negative integer
4
    '''
5
    # Your code here
6
    if(N < 17):
7
        if(N == 7):
8
            return 1
9
        else:
10
            return 0
11
    else:
12
        if(N % 10 == 7):
13
            return (1 + count7(int(N/10)))
14
        else:
15
            return (count7(int(N/10)))
Press ESC then TAB or click outside of the code editor to exit
correctCorrect
Test results
CORRECT See full output

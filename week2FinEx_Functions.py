
# A function to calculate a square of a number
def square(x):
    return x**2
print(square(3))

# A function to calculate ax^2+bx+c
def evalQuadratic(a, b, c, x):
    return((a*(x**2)+b*x+c))
print(evalQuadratic(2, 3, 4, 5))

# A function to calculate fourth power of a number
def fourthPower(x):
    return square(square(x))

print(fourthPower(3))

# A function that takes in a number and return True when the number is odd and False otherwise.
def odd(x):
    if(x%2==0):
        return True
    else:
        return False
print(odd(2))

# In Problem 1, we computed an exponential by iteratively executing successive multiplications. We can use the same idea, but in a recursive function.Write a function recurPower(base, exp) which computes  by recursively calling itself to solve a smaller version of the same problem, and then multiplying the result by base to solve the initial problem.This function should take in two values - base can be a float or an integer; exp will be an integer . It should return one numerical value. Your code must be recursive - use of the ** operator or looping constructs is not allowed.
def recurPower(base, exp):
    if exp==0:
        return 1
    else:
        return base*(recurPower(base, exp-1))
print(recurPower(4, 4))

#Write an iterative function iterPower(base, exp) that calculates the exponential  by simply using successive multiplication. For example, iterPower(base, exp) should compute  by multiplying base times itself exp times. Write such a function below. This function should take in two values - base can be a float or an integer; exp will be an integer  0. It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed.
def iterPower(base, exp):
    temp=1
    for i in range(exp):
        temp*=base
    return temp     
print(iterPower(3,4))

# The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,gcd(2, 12) = 2,gcd(6, 12) = 6,gcd(9, 12) = 3 and gcd(17, 12) = 1 A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:If b = 0, then the answer is aOtherwise, gcd(a, b) is the same as gcd(b, a % b)See this website for an example of Euclid's algorithm being used to find the gcd.Write a function gcdRecur(a, b) that implements this idea recursively. This function takes in two positive integers and returns one integer.
def gcdRecur(a, b):
    if b==0:
        return a
    return gcdRecur(b, a%b)
print(gcdRecur(17, 12))

# The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,gcd(2, 12) = 2,gcd(6, 12) = 6, and gcd(9, 12) = 3 and gcd(17, 12) = 1Write an iterative function, gcdIter(a, b), that implements this idea. One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1.
def gcdIter(a, b):
    temp = min(a,b)
    while temp>0:
        if(a%temp==0 and b%temp==0):
            return temp
        else:
            temp-=1
print(gcdIter(9, 12))

#We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical order.First, test the middle character of a string against the character you're looking for (the "test character"). If they are the same, we are done - we've found the character we're looking for!.If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's < function.).Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. char will be a single character and aStr will be a string that is in alphabetical order. The function should return a boolean value..As you design the function, think very carefully about what the base cases should be.

def isIn(char , aStr):
    aStrSorted = sorted(aStr)
    low = 0
    high = len(aStrSorted)
    mid = int((low + high) / 2)
    
    if len(aStr) <=0:
        return False
    
    elif char == aStrSorted[mid]:
        return True
    
    if char > aStrSorted[mid]:
        low = mid
        return(isIn(char , aStrSorted[low:high]))
     
    else:
        high = mid
        return(isIn(char , aStrSorted[low:high]))
        
print(isIn('a','lmab'))


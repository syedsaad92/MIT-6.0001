#Problem 4
#Write a Python function that creates and returns a list of prime numbers between 2 and N, inclusive, sorted in increasing order. A prime number is a number that is divisible only by 1 and itself. This function takes in an integer and returns a list of integers.

def primes_list(N):
    '''
    N: an integer
    '''
    # Your code here
    temp = []
    for i in range(2,N+1):           
        for j in range(2,i-1):
            if i%j==0: 
                break
        else:
            temp.append(i)
    return(temp)

print(primes_list(12)) 

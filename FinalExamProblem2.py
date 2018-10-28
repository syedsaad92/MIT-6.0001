#Problem 2
#
#Problem 2-1
#You have the following class hierarchy:
#
#class A(object):
#    def foo(self):
#        print('hi')
#class B(A):
#    def foo(self):
#        print('bye')
#          
#Which of the following is correct?
#
#When a = A() we say that a is an instance of A
#When b = B() we say that b is a subclass of A incorrect
#Both of the above
#Neither of the above
#
#Problem 2-2
#Consider the function f below. What is its Big O complexity?
#
#def f(n):
#    def g(m):
#        m = 0
#        for i in range(m):
#            print(m)
#    for i in range(n):
#        g(n)
#
#O()
#O(log(n))
#O(n)
#O(n^2) incorrect
#
#Problem 2-3
#A dictionary is an immutable object because its keys are immutable.
#True incorrect
#False because its keys can be mutable
#False because a dictionary is mutable
#
#Problem 2-4
#Consider the following two functions and select the correct choice below:
#
#def foo_one(n):
#    """ Assume n is an int >= 0 """
#    answer = 1.0
#    while n > 1:
#        answer *= n
#        n -= 1
#    return answer
#
#def foo_two(n):
#    """ Assume n is an int >= 0 """
#    if n <= 1: 
#        return 1.0
#    else: 
#        return n*foo_two(n-1)
#
#The worst case Big Oh time complexity of foo_one is worse than the worst case Big Oh time complexity of foo_two.
#The worst case Big Oh time complexity of foo_two is worse than the worst case Big Oh time complexity of foo_one. incorrect
#The worst case Big Oh time complexity of foo_one and foo_two are the same.
#Impossible to compare the worst case Big Oh time complexities of the two functions.
#
#Problem 2-5
#The complexity of 1^n + n^4 + 4n + 4 is
#
#
#constant
#logarithmic
#linear
#polynomial correct
#exponential
# Submit You have u

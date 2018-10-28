#Problem 3
#Implement a function that meets the specifications below.

#def sum_digits(s):
#    """ assumes s a string
#        Returns an int that is the sum of all of the digits in s.
#          If there are no digits in s it raises a ValueError exception. """
#    # Your code here
#For example, sum_digits("a;35d4") returns 12.

#Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    integer = 0
    nonInteger = 0
    for element in s:            
      try:
        integer += int(element)
      except:
        nonInteger += 1
    if nonInteger != len(s):
      return integer
    else:
      raise ValueError
      
#print(sum_digits("a;35d4"))

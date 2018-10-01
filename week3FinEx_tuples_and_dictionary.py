# Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other element of the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').

def oddTuples(aTup):
    return aTup[::2]
    
print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))    

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = abs(L[i])
    return L
    
def mod(a):
    return abs(a)
    
testList = [1, -4, 8, -9]
print(applyToEach(testList, mod))

# Consider the following sequence of expressions: animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}.animals['d'] = ['donkey'] .animals['d'].append('dog'). animals['d'].append('dingo'). We want to write some simple procedures that work on dictionaries to return information. First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary. For example:
def how_many(aDict):
    num_of_values = 0
    for animal in aDict.values():
        for sub_animal in animal:
            num_of_values += 1
    return num_of_values

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']} 
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')       
print(how_many(animals))

"""Consider the following sequence of expressions:
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
We want to write some simple procedures that work on dictionaries to return information.
This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.
Example usage:
>>> biggest(animals)
'd'
If there are no values in the dictionary, biggest should return None."""

def biggest(aDict):
    result = 1
    for key in aDict.keys():
        if len(aDict[key]) > result:
            result = key
            return result
        
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(biggest(animals))


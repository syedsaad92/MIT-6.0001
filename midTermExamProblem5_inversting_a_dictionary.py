#Problem 5
#20.0/20.0 points (graded)
#Write a function called dict_invert that takes in a dictionary with immutable values and returns the inverse of the dictionary. The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. The value for a key in the inverse dictionary is a sorted list of all keys in d that have the same value in d.
#
#Here are some examples:
#
#If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
#If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
#If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    invert = {}
    for num in d.keys():
        if d[num] in invert:
            invert[d[num]].append(num)
        else:
            invert[d[num]] = [num]
    for num in invert.values():
        num.sort()
    return invert

d = {1:10, 2:20, 3:30, 4:30}
print(dict_invert(d))

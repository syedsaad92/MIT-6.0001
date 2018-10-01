# Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.
def getAvailableLetters(lettersGuessed):
    temp = ''
    import string
    alphabets = string.ascii_lowercase
    for char in alphabets:
        if char not in lettersGuessed:
            temp += char
    return temp
    
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))

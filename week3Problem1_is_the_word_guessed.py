# Please read the Hangman Introduction before starting this problem. We'll start by writing 3 simple functions that will help us easily code the Hangman problem. First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.
def isWordGuessed(secretWord , lettersGuessed):
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's'] 
print(isWordGuessed(secretWord , lettersGuessed)) 

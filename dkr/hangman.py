# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_letters = ""
    for i in secret_word:
        if i in letters_guessed:
            guessed_letters = guessed_letters + i 
        else:
            guessed_letters = guessed_letters + "_ "
    return guessed_letters




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    for i in alphabet:
        if i in letters_guessed:
            alphabet = alphabet.replace(i, "")
    return alphabet

    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    vowels = ["a", "e", "i", "o", "u"]
    attempts = 6
    fails = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    print("-" * 20)
    while attempts > 0 and not is_word_guessed(secret_word, letters_guessed):
        print(f"You have {attempts} guesses left")
        print(f"You have {fails} warnings left")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        letter = input("Please guess a letter: ")
        print("-" * 20)
        if len(letter) > 1 or not letter.isalpha() or letter in letters_guessed:
            if len(letter) > 1 or not letter.isalpha():
                print("Enter only letter!")
                print(f"{get_guessed_word(secret_word, letters_guessed)}")
            elif letter in letters_guessed:
                print("Enter only letters, which you didn`t enter before!")
                print(f"{get_guessed_word(secret_word, letters_guessed)}")
            fails = fails - 1
            if fails == -1:
                print("You have no warnings left so you loose one guess.")
                fails, attempts = 0, attempts - 1
        elif letter not in secret_word:
            letters_guessed.append(letter)
            attempts = attempts - 2 if letter in vowels else attempts - 1
            print(f"Oops! That letter not in my word: {get_guessed_word(secret_word, letters_guessed)}")
        else:
            letters_guessed.append(letter)
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")

    if is_word_guessed(secret_word,letters_guessed):
        print("-" * 20)
        print("CONGRATULATIONS, YOU WON!")
        print(f"Your total score for this game is: {len(set(secret_word)) * attempts}")
    else:
        print("-" * 20)
        print("GAME OVER!!!")
        print(f"Sorry, you lost, the word was {secret_word}")
        print("Better next time!")  

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word: str, other_word: str) -> bool:
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for my_char, other_char in zip(my_word,other_word):
        if my_char != "_" and my_char != other_char:
            return False
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    match = []
    for i in wordlist:
           if match_with_gaps(my_word, i):
               match.append(i)
    if len(match) == 0:
        print("No matches found")
    else:
        for i in match:
            print(i, end=" ")
    print("")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    vowels = ["a", "e", "i", "o", "u"]
    attempts = 6
    fails = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    print("-" * 20)
    while attempts > 0 and not is_word_guessed(secret_word, letters_guessed):
        print(f"You have {attempts} guesses left")
        print(f"You have {fails} warnings left")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        letter = input("Please guess a letter: ")
        print("-" * 20)
        if len(letter) > 1 or not letter.isalpha() or letter in letters_guessed:
            if len(letter) > 1 or not letter.isalpha():
                print("Enter only letter!")
                print(f"{get_guessed_word(secret_word, letters_guessed)}")
                if letter == "*":
                    fails = fails + 1
                    print("Mathes:", end=" ")
                    show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            elif letter in letters_guessed:
                print("Enter only letters, which you didn`t enter before!")
                print(f"{get_guessed_word(secret_word, letters_guessed)}")
            fails = fails - 1
            if fails == -1:
                print("You have no warnings left so you loose one guess.")
                fails, attempts = 0, attempts - 1
        elif letter not in secret_word:
            letters_guessed.append(letter)
            attempts = attempts - 2 if letter in vowels else attempts - 1
            print(f"Oops! That letter not in my word: {get_guessed_word(secret_word, letters_guessed)}")
        else:
            letters_guessed.append(letter)
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")

    if is_word_guessed(secret_word,letters_guessed):
        print("-" * 20)
        print("CONGRATULATIONS, YOU WON!")
        print(f"Your total score for this game is: {len(set(secret_word)) * attempts}")
    else:
        print("-" * 20)
        print("GAME OVER!!!")
        print(f"Sorry, you lost, the word was {secret_word}")
        print("Better next time!")  



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

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

WORDLIST_FILENAME = "wordsH.txt"
game_start = True
num_guesses = 6
num_warnings = 3
guessed = [] #letters guessed by user
result = None #if result=1 it's a win, or else if result=0 it's a loss
guess = None # user's guess
version = 0
hints_guessed = [] # copy of guessed


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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    count_right = 0 #this variable keeps track of the number of correct letters
    for char in secret_word:
        if char in letters_guessed:
            count_right+=1
    if count_right == len(secret_word):
        return True
    else:
        return False
#print(is_word_guessed('apple',['a','b','x','r','o']))




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    global guess
    global num_guesses
    global guessed
    global num_warnings
    global hints_guessed
    if str.isalpha(guess):
        letters_guessed+=guess
        hints_guessed += guess
    output='' #this is the string I will show to the user as the word
    for char in secret_word:
        if char in letters_guessed:
           output+=char
        else:
            output+='_ '
    if guessed.__contains__(guess):
        guessed.remove(guess)

    if guess == '*' and version == 1:
        match_with_gaps(output)
    elif not str.isalpha(guess):
        if num_warnings > 0:
            num_warnings -= 1
            print(f"That is not a letter in the alphabet. "
                  f"You have {num_warnings} warning(s) left: {output}")
        else:
            num_guesses-=1
    elif guess in guessed:
        if num_warnings > 0:
            num_warnings -= 1
            print(f"You already guessed that letter. "
                  f"You have {num_warnings} warning(s) left: {output}")
        else:
            if guess in 'aeiou':
                num_guesses -= 2
            else:
                num_guesses -= 1
    else:
        guessed += [guess]
        if secret_word.__contains__(guess):
            print(f"Good guess: {output}")
        else:
            print(f"Oops! That letter is not in my word: {output}")
            if guess in 'aeiou':
                num_guesses -= 2
            else:
                num_guesses-=1
    if version == 1:
        hangman_with_hints(secret_word)
    else:
        hangman(secret_word)


#print(get_guessed_word('apple',['a','b','x','r','o','p']))




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    remaining='' #string that contains all letters not yet guessed
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            remaining+=char
    return remaining

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #declaring global variables
    global game_start
    global guess
    global guessed
    global num_guesses
    global num_warnings
    if game_start:
        print(f"Welcome to the game Hangman!\nI am thinking of a word that "
              f"is {len(secret_word)} letters long.\n-------------")
        game_start = False
    if not game_start:
        if num_guesses > 0 and is_word_guessed(secret_word,guessed):
            uniques=0 #contains the unique letters in secret_word
            for char in secret_word:
                if secret_word.count(char) == 1:
                    uniques+=1
            score=num_guesses*uniques
            print(f"Congratulations, you won! Your score is {score}.")
        elif num_guesses > 0:
            print(f"You have {num_guesses} guess(es) left.\nAvailable letters:"
                  f"{get_available_letters(guessed)}\n------------")
            guess = input("Please enter a guess: ")
            guess = guess.lower()
            get_guessed_word(secret_word,guessed)
        else:
            print(f"You are out of guesses! Sorry, you lost. The word was {secret_word}")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    possible = []
    my_word = my_word.replace(' ','')
    line_count = 0
    #ordlist=["apple","aoalq","eo","appbe"]
    for word in wordlist:
        sim_count = 0 #number of similar characters between the guessed word and the word from wordlist
        index_my_word = 0
        if len(word) == len(my_word):
            for char in word:
                if (char == my_word[index_my_word] or my_word[index_my_word]=='_') and (word.count(char) == my_word.count(char) or my_word.count(char) == 0):
                    if char in hints_guessed: #checking if the letter has been guessed, in which case we will only add the word if the real word contains the guessed letter
                        if secret_word.__contains__(char):
                            sim_count+=1
                    else:
                        sim_count+=1
                index_my_word+=1
                #print(f"you've guessed {hints_guessed}")

            if sim_count == len(word):
                #print(f"word={word}")
                line_count += 1
                possible.append(word)
                if line_count % 5 == 0:
                    possible.append("\n")
                #print(possible[0])
    #print(f"possible{possible}")
    #print(f"posa {possible[0]}")
    print(f"Possible words include:\n "+" ".join(possible))







def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



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
    # FILL IN YOUR CODE HERE AND DELETE "pass
    global game_start
    global guess
    global guessed
    global num_guesses
    global num_warnings
    if game_start:
        print(f"Welcome to the game Hangman!\nI am thinking of a word that "
              f"is {len(secret_word)} letters long.\n-------------")
        game_start = False
    if not game_start:
        if num_guesses > 0 and is_word_guessed(secret_word, guessed):
            uniques = 0  # contains the unique letters in secret_word
            for char in secret_word:
                if secret_word.count(char) == 1:
                    uniques += 1
            score = num_guesses * uniques
            print(f"Congratulations, you won! Your score is {score}.")
        elif num_guesses > 0:
            print(f"You have {num_guesses} guess(es) left.\nAvailable letters:"
                  f"{get_available_letters(guessed)}\n------------")
            guess = input("Please enter a guess: ")
            guess = guess.lower()
            get_guessed_word(secret_word, guessed)
        else:
            print(f"You are out of guesses! Sorry, you lost. The word was {secret_word}")


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    #pass
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    #match_with_gaps(secret_word)
    valid=False
    while not valid:
        version = int(input("Would you like to play with hints (1) or without hints (2)? "))
        if version == 1:
            hangman_with_hints(secret_word)
            valid=True
        elif version == 2:
            hangman(secret_word)
            valid=True



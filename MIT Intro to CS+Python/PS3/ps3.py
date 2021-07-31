# 6.0001 Problem Set 3
# The 6.0001 Word Game
# Name: Nakul Nayak

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = None
TOTAL_HANDS = None
final_score = 0
total_score = 0
score_bef = 0
score_aft = 0

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10,'*':0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    
    #pass  # TO DO... Remove this line when you implement this function
    word = str.lower(word) #since we cannot assume case I convert to lowercase
    comp_1 = 0 #first component of score (sum of letter points)
    comp_2 = 0 #second component of score (1 or 7*wordlen-3*(n-wordlen))
    score = 0 #score for word that I will return

    if word != "":
        for letter in word:
            comp_1 += SCRABBLE_LETTER_VALUES.get(letter,0)
        comp_2 = 7*len(word)-3*(n-len(word))
        if comp_2 < 1:
            comp_2 = 1
    score = comp_1 * comp_2

    return score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    hand['*'] = 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n-1):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    #print(hand)
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    updated_h = hand.copy()  #updated_h is the updated hand, I will return this variable
    word = str.lower(word)
    for letter in word:
        if hand.get(letter,0) !=0:
            updated_h[letter]-=1
    return updated_h


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    valid = True
    copy_hand = hand.copy()
    copy_word = str.lower(word)
    in_list = False

    if copy_word.__contains__('*'):
        for letter in VOWELS:
            if copy_word.replace('*',letter) in word_list:
                #print("The guessed word is "+copy_word)
                #print(copy_word.replace('*',letter)+" is in word_list")
                #print(f"index= "+str(word_list.index(copy_word.replace('*',letter))))
                in_list = True

    if copy_word in word_list or in_list:
        for letter in copy_word:
            if copy_hand.get(letter, 0) == 0:
                valid = False
            else:
                copy_hand[letter]-=1
    else:
        valid = False
    return valid
#wingy = load_words()
#is_valid_word("Rapture",{'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1},wingy)

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    hand_length = 0
    for key in hand:
        hand_length += hand[key]
    return hand_length

def play_hand(hand, word_list,replayed,subs,beginning,done_replay,HAND_SIZE):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    hand_length = calculate_handlen(hand)
    word = ""
    user_sub = "" #user's response regarding whether he wants to substitute or not
    rm_lett = "" #letter that user wants to remove
    points_earned = 0
    global total_score
    global final_score
    global score_bef
    global score_aft
    hand_output = ""
    #print(f"subs is {subs}")
    # As long as there are still letters left in the hand:
    while hand_length > 0:
        hand_output=""
        for letter in hand:
            for x in range(hand[letter]):
                hand_output += letter
        print(f"Current hand: {hand_output}")
        if (not subs) and beginning:
            #print(f"subs is {subs} and beginning is {beginning}")
            user_sub = input("Would you like to substitute a letter? ").lower()
            beginning = False
            if user_sub == "yes":
                subs = True
                rm_lett = input("Which letter would you like to replace? ")
                hand = substitute_hand(hand,rm_lett)
                play_hand(hand,word_list,replayed,subs,beginning,done_replay,HAND_SIZE)
                #print(f"word is {word}")
                if word == "":
                    return
        word = input("Enter a word, or \"!!\", to indicate that you are finished: ")
        # If the input is two exclamation points:
        if word == "!!":
            #print("pangish")
            break
        elif is_valid_word(word, hand, word_list):
            points_earned = get_word_score(word, hand_length)
            total_score += points_earned
            final_score += points_earned
            if replayed and not done_replay:
                score_bef = total_score
            if done_replay:
                score_aft = total_score
                if score_aft > score_bef:
                    total_score -= score_bef
                    final_score -= score_bef
                else:
                    total_score -= score_aft
                    final_score -= score_aft
            #print(f"score before = {score_bef},score after = {score_aft}")
            print(f"\"{word}\" earned {points_earned} points. Total: {total_score} points\n-------------------------------------")
            hand = update_hand(hand, word)
            hand_length = calculate_handlen(hand)
        else:
            print("That is not a valid word.")
            hand = update_hand(hand, word)
            hand_length = calculate_handlen(hand)
    if word=="!!":
        print(f"Total score: {total_score} points\n-------------------------------------")
        print(f"Final score is {final_score}")
    elif hand_output == "":
        print(f"Ran out of letters. Total score: {total_score} points\n-------------------------------------")
        print(f"Final score is {final_score}")
    else:
        print(f"Final score is {final_score}")


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    available = "" #all available letters that can replace $letter
    if letter in hand.keys():
        for alpha in string.ascii_lowercase:
            if alpha not in hand.keys():
                available += alpha
        chosen_lett = random.choice(available)
        freq_letter = hand[letter]
        hand.pop(letter,None)
        hand[chosen_lett]=freq_letter
        #print(hand)
    else:
        print("This letter is not in the hand. You lost your subsitution chance!")
    return hand
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    TOTAL_HANDS = int(input("Enter total number of hands you want to play: "))
    HAND_SIZE = int(input("Enter number of letters you want per hand: "))
    hand = deal_hand(HAND_SIZE)
    replayed = False
    subs = False #whether or not user has already substituted
    beginning = True #whether or not it is the first play of the hand
    redo=""
    roundcount = 1
    in_case_total_score = 0
    done_replay = False

    global total_score
    global final_score
    global score_bef
    global score_aft

    while TOTAL_HANDS > 0:
        print(f"ROUND {roundcount}")
        if replayed:
            done_replay = True
        play_hand(hand,word_list,replayed,subs,beginning,done_replay,HAND_SIZE)
        if not replayed:
            redo = input("Would you like to replay the hand? ").lower()
        if redo == "yes":
            score_bef = total_score
            replayed = True
            beginning = False
        else:
            TOTAL_HANDS-=1
            hand = deal_hand(HAND_SIZE)
            beginning = True
            roundcount += 1
            score_bef = 0
            score_aft = 0
            total_score = 0
        redo = ""
    print(f"-------------------------------------\nTotal score over all hands:{final_score}")


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    #play_hand(deal_hand(HAND_SIZE),word_list)
    #play_hand({"*": 1, "u": 2, "e": 1, "n": 1, "r": 1, "w": 1}, word_list)
    #play_hand({"a":1,"c":1,"f":1,"i":1,"*":1,"t":1,"x":1},word_list)
    play_game(word_list)

# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
#   >>> is_word(load_words(WORDLIST_FILENAME), 'bat')
    True
#   >>> is_word(load_words(WORDLIST_FILENAME), 'asdf')
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
ALL_LETTERS = string.ascii_lowercase + string.ascii_uppercase

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        cp_valid = self.valid_words
        return cp_valid

    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        dict_keys = {'a':vowels_permutation[0],'e':vowels_permutation[1],'i':vowels_permutation[2],
                     'o':vowels_permutation[3],'u':vowels_permutation[4],'A': vowels_permutation[0].upper(),
                     'E':vowels_permutation[1].upper(),'I':vowels_permutation[2].upper(),'O':vowels_permutation[3].upper(),
                     'U':vowels_permutation[4].upper()}
        for letter in ALL_LETTERS:
            if letter not in vowels_permutation:
                dict_keys[letter] = letter

        return dict_keys


    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        encrypted_text = ''
        for char in self.message_text:
            if char in ALL_LETTERS:
                encrypted_text += transpose_dict[char]
            else:
                encrypted_text += char
        return encrypted_text

class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)
    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        poss_perm = get_permutations('aeiou') #list that stores all possible vowel permutations. Will use this to iterate over each possible vowel encryption.
        temp_count = 0  # used to count num of valid words
        temp_msg = ''  # used to store current message
        final_info = ['',0] #will store the previous and final message in the 0th index and the previous and final count of valid words
        for perm in poss_perm:
            temp_count = 0
            decrypt_dict = self.build_transpose_dict(perm)
            temp_msg = self.apply_transpose(decrypt_dict)
            for word in temp_msg.split():
                if is_word(self.valid_words,word):
                    temp_count += 1
            if final_info[1] < temp_count:
                final_info[0] = temp_msg
                final_info[1] = temp_count
        if final_info[1] == 0:
            return self.message_text
        return final_info[0]





if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutations = ["eaiuo","auioe","iuaeo"]
    for perm in permutations:
        enc_dict = message.build_transpose_dict(perm)
        print("Original message:", message.get_message_text(), "Permutation:", perm)
        print("Expected encryption:", "Hallu Wurld!")
        print("Actual encryption:", message.apply_transpose(enc_dict))
        enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
        print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE

# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
#    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    #base case
    if len(sequence) <= 1:
        return [sequence]
    else:
       final_list=[]
       #sequence = sequence[1:]
       first_char = sequence[0]
       rest = sequence[1:]
       perms_list = get_permutations(rest)
       for word in perms_list:
           for ind in range(len(word)+1):
               new_word = word[0:ind]+first_char+word[ind:]
               final_list.append(new_word)
    return final_list

if __name__ == '__main__':
#    #EXAMPLE
     example_input = 'abc'
     poss = []
     print('Input:', example_input)
     print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
     print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

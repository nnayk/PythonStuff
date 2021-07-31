from Q4 import tree,root,branches,print_tree
def has_path(t, word,first=True):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    >>> has_path(greetings, 'hint')
    False
    """
    assert len(word) > 0, 'no path for empty word.'
    "*** YOUR CODE HERE ***"
    if first:
        t=tree('h', [tree('i'),tree('e', [tree('l', [tree('l', [tree('o')])]),tree('y')])])
    #if len(t)==0 and len(word)!=0:
    #    return False
    #print(f"te={t},word={word},first={first}")
    if len(word)==1 and root(t)==word:
        #print("1")
        return True

    #if (len(t)==1 or len(t[0])==1) and len(word)>1:
     #   return False

    if len(word)>1 and root(t)==word[0]:
        #print("2")
        t=branches(t)
        word=word[1:]

    elif root(t)!=word[0] and first:
        #print("3")
        return False

    first = False

    #hello
    #sigli=[['e', ['l', ['l', ['o']]], ['y']]]
    #branch=['e', ['l', ['l', ['o']]], ['y']]
    #lett=e,word=ello
    #branchita=['e', ['l', ['l', ['o']]], ['y']]

    #print(f"sigli={branches(t)}")
    for branch in t:
        #print(f"brancho={branch}")
        for ind,lett in enumerate(branch):
            #print(f"lett={lett},word={word}")
            if lett==word[0] and len(word)==1:
                return True
            elif lett==word[0]:
                #print(f"branchita={branch}")
                if len(word)>1 and len(branch)>1:
                    branch.pop(ind)
                    return has_path(branch,word[1:],first)
    return False

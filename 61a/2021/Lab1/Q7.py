def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    word=str(n)

    index=0

    while index<len(word):
        if index<len(word)-1:
            if word[index]==word[index+1] and word[index]=='8':
                return True
        index+=1
    return False
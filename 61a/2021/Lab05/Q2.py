def map(fn, lst):
    """Maps fn onto lst using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> map(lambda x: x * x, original_list)
    >>> original_list
    [25, 1, 4, 0]
    """
    "*** YOUR CODE HERE ***"
    #x=lst
    for ind,ele in enumerate(lst):
        lst[ind]=fn(ele)
    #return lst
    #print(x)

map()
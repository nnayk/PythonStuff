def swap(a, b):
    """Swap the contents of lists a and b.

    >>> a = [1, 'two', 3]
    >>> b = [4, [5, 6]]
    >>> swap(a, b)
    >>> a
    [4, [5, 6]]
    >>> b
    [1, 'two', 3]
    """
    "*** YOUR CODE HERE ***"
    temp=list(a)

    popper(a)
    create(a,b)

    popper(b)
    create(b,temp)

def popper(lst,i=0):
    while i<len(lst):
        lst.pop(i)

def create(make,model):
    for ele in model:
        make.append(ele)



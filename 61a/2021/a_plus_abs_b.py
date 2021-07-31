def a_plus_abs_b(a,b):
    """
    >>> a_plus_abs_b(2,3)
    5
    >>> a_plus_abs_b(2,-3)
    5
    """
    if b<0:
        f=a-b
    else:
        f=a+b
    return f


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n<=3:
        return n
    else:
        return g(n-1)+2*g(n-2)+3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    True
    """
    "*** YOUR CODE HERE ***"
    sol=0
    factor=1
    cp_n=n
    while cp_n>=n-3:
        if cp_n<=3:
            sol+=n
        else:
            cp_cp=cp_n
            while cp_n >= n - 3:
                if cp_n <= 3:
                    sol += n
                if cp_n == n - 2:
                    factor = 2
                elif cp_n == n - 3:
                    factor = 3

        cp_n-=1
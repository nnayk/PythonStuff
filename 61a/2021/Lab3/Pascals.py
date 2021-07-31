def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    "*** YOUR CODE HERE ***"
    try:
        return fact(row)//(fact(row-column)*fact(column))
    except ZeroDivisionError:
        return 0

def fact(n):
       try:
            if n==0 or n==1:
                return 1
            return n*fact(n-1)
       except RecursionError:
            return 0
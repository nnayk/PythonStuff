class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0,previous=1):
        self.value = value
        self.previous=previous

    def next(self):
        "*** YOUR CODE HERE ***"
        return Fib(self.previous+self.value,self.value)

    def __repr__(self):
        return str(self.value)

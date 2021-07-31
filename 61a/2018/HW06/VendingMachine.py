class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"

    def __init__(self,name,cost,stock=0,balance=0):
        self.name=name
        self.cost=cost
        self.stock=stock
        self.balance=balance


    def vend(self):
        response=''
        if self.stock==0:
            return 'Machine is out of stock.'

        if self.stock>0:
            if self.balance==self.cost:
                self.balance=0
                self.stock-=1
                return 'Here is your {0}.'.format(self.name)
            elif self.balance>self.cost:
                cp_bal=self.balance
                self.balance=0
                self.stock-=1
                return 'Here is your {0} and ${1} change.'.format(self.name,cp_bal-self.cost)
            else:
                return 'You must deposit ${0} more.'.format(self.cost-self.balance)

    def deposit(self,amount):
        #print(f"self.stock={self.stock}")
        if self.stock==0:
            return 'Machine is out of stock. Here is your ${0}.'.format(amount)
        else:
            #print("self.balance={0}".format(self.balance))
            self.balance+=amount
            return 'Current balance: ${0}'.format(self.balance)

    def restock(self,quant):
        self.stock+=quant
        return 'Current '+self.name+' stock: '+str(self.stock)




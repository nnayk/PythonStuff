from Q4 import tree,branches,root
def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    x=str(t)
    ordered=""
    fin=[]
    for char in x:
        if not(char=='[' or char==']') and not(char==','):
            ordered+=char

    for char in ordered:
        try:
            fin.append(int(char))
        except:
            None
    return fin
def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    ordered=[]
    #print(t)
    for ele in t:
        #print(f"ele={ele}")
        if type(ele) == int:
            ordered.append(ele)
            #t.pop(0)
            #print(f"t={t}")

        else:
            for num in ele:
                #print(f"num={num}")
                try:
                    ordered.append(int(num))
                except:
                    ordered.append(num[0])
    return ordered








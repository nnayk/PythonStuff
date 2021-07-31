#2021 summer, finding berries, recursive implementation
def berry_finder(t):
    """Returns True if t contains a node with the value 'berry' and
    False otherwise.

    >>> scrat = tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
    >>> berry_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = tree(1, [tree('berry',[tree('not berry')])])
    >>> berry_finder(t)
    True
    """
    "*** YOUR CODE HERE ***"
    #print(f"t={t}")
    return is_berry(t)
def tree(root,branches=[]):
    return [root]+list(branches)

def branches(tree):
    return tree[1:]

def root(tree):
    return tree[0]

def is_berry(tree,found=False,in_call=False):
    #print(f"tree is a list: {type(tree)==list}, tree is ['berry']:{tree==['berry']}")
    if len(str(tree))>1 and root(tree)=='berry':
        return True
    elif type(tree)==list and tree==['berry']:
        return True
    else:
        if in_call:
            return False
        for branch in branches(tree):
            in_call=True
            found = is_berry(branch)
            if found==True:
                return found
    return found


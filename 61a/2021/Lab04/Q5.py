#2021 summer, finding berries
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
    #print(look(t))
    if 'berry' in look(t) or ['berry'] in look(t):
        return True
    return False
def tree(root,branches=[]):
    return [root]+list(branches)
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
def look(tree):
    #print(tree)
    nodes=[]
    try:
        for ele in tree:
            if len(str(ele))>1 and type(ele)==list:
                for node in ele:
                    nodes.append(node)
            else:
                    nodes.append(ele)
        #print(nodes)
        return nodes
    except TypeError:
        #print('kaj')
        nodes=[x for x in tree]
        #print(nodes)
        return nodes

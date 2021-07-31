def replace_loki_at_leaf(t, lokis_replacement):
    """Returns a new tree where every leaf value equal to "loki" has
    been replaced with lokis_replacement.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('loki'),
    ...                         tree('freya')]),
    ...                   tree('frigg',
    ...                        [tree('loki')]),
    ...                   tree('loki',
    ...                        [tree('sif'),
    ...                         tree('loki')]),
    ...                   tree('loki')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_loki_at_leaf(yggdrasil, 'freya'))
    odin
      balder
        freya
        freya
      frigg
        freya
      loki
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    "*** YOUR CODE HERE ***"
    #print(t)
    roo=root(t)
    tmp_br=[]
    all_br=[]
    ele=[]
    #print(t[0])
    look=True
    for branch in branches(t):
        look=True
        if len(branch)==1 and branch==["loki"]:
            branch=[lokis_replacement]
            tmp_br.append(branch)
            all_br.append(branch)
            tmp_br=[]
            look=False
        if look:
            for ele in branch:
                #print(f"ele={ele}")
                if ele==["loki"]:
                    ele=[lokis_replacement]
                    #print(f"yelay={ele}")
                tmp_br.append(ele)
                #print(f"tmp_br is {tmp_br}")
            all_br.append(tmp_br)
            tmp_br=[]
    return tree(roo,all_br)

def copy_tree(tree):
    return list(tree)

def tree(root,branches=[]):
    return [root]+list(branches)

def root(tree):
    #print(tree)
    return tree[0]

def branches(tree):
    return tree[1:]

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    #print("as",t)
    print('  ' * indent + str(root(t)))
    for b in branches(t):
        print_tree(b, indent + 1)
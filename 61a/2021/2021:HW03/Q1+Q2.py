def mobile(left, right):
    """Construct a mobile from a left arm and a right arm."""
    assert is_arm(left), "left must be a arm"
    assert is_arm(right), "right must be a arm"
    return ['mobile', left, right]

def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'

def left(m):
    """Select the left arm of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]

def right(m):
    """Select the right arm of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]

def arm(length, mobile_or_planet):
    """Construct a arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]

def is_arm(s):
    """Return whether s is a arm."""
    return type(s) == list and len(s) == 3 and s[0] == 'arm'

def length(s):
    """Select the length of a arm."""
    assert is_arm(s), "must call length on a arm"
    return s[1]

def end(s):
    """Select the mobile or planet hanging at the end of a arm."""
    assert is_arm(s), "must call end on a arm"
    return s[2]
def planet(size):
    """Construct a planet of some size."""
    assert size > 0
    "*** YOUR CODE HERE ***"
    return ["planet",size]


def size(w):
    """Select the size of a planet."""
    assert is_planet(w), 'must call size on a planet'
    "*** YOUR CODE HERE ***"
    return w[1]

def is_planet(w):
    """Whether w is a planet."""
    return type(w) == list and len(w) == 2 and w[0] == 'planet'
def examples():
    t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
    #print(t)
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                              arm(3, planet(2)))))
    #print(u)
    v = mobile(arm(4, t), arm(2, u))
    #print(v)
    return (t, u, v)

def total_weight(m):
    """Return the total weight of m, a planet or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_planet(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a planet"
        return total_weight(end(left(m))) + total_weight(end(right(m)))
def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(arm(3, t), arm(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(arm(1, v), arm(1, w)))
    False
    >>> balanced(mobile(arm(1, w), arm(1, v)))
    False
    """
    "*** YOUR CODE HERE ***"
    if is_planet(m):
        #print(f"In planet {m}")
        return True
    else:
        #print(f'not {m}')
        #print(m)
        left,l_arm_len = get_left(m)
        right,r_arm_len=get_right(m)
        #print(f"Left={left},Right={right}")
        #print(f'left arm={l_arm_len} and right arm={r_arm_len}')

        if balanced(left):
            if balanced(right):
                return torque(left,l_arm_len)==torque(right,r_arm_len)
        return False
def get_left(m):
    left = m[1][2]
    l_arm_len = m[1]
    return left,l_arm_len
def get_right(m):
    r_arm_len = m[2]
    right = m[2][2]
    return right,r_arm_len

def torque(mob,arm_len):
    tor=total_weight(mob)*length(arm_len)
    return tor


#######################################
#################   Q3   ##################
#######################################
def totals_tree(m,branches,left_b,right_b,first=True,root=0):
    """Return a tree representing the mobile with its total weight at the root.

    >>> t, u, v = examples()
    >>> print_tree(totals_tree(t,branches=[],left_b=[],right_b=[]))
    3
      2
      1
    >>> print_tree(totals_tree(u,branches=[],left_b=[],right_b=[]))
    6
      1
      5
        3
        2
    >>> print_tree(totals_tree(v,branches=[],left_b=[],right_b=[]))
    9
      3
        2
        1
      6
        1
        5
          3
          2
    """
    "*** YOUR CODE HERE ***"
    if first:
        root=total_weight(m)

    left_child=left_part(m)
    right_child=right_part(m)
    #print(f'm={m}')
    #print(f"left_child={left_child},right child={right_child}")
    #print("BEFORE BRANCHES",branches)




    if is_mobile(left_child) and is_mobile(right_child):
        left_b.append(total_weight(left_child))
        right_b.append([total_weight(right_child)])
        totals_tree(left_child,branches,left_b,right_b,False,root)
        totals_tree(right_child,branches,left_b,right_b, False, root)

    if is_planet(left_child) and is_mobile(right_child):
        print(f"branches billu={branches}")
        left_b.append(size(left_child))
        #print(f"sizey={size(left_child)}")
        right_b.append(total_weight(right_child))
        #print(f"righty ={total_weight(right_child)}")
        #print(f"chal branches={branches}")
        branches.append(left_b)
        left_b = []
        totals_tree(right_child,branches,left_b,right_b,False,root)

    if is_planet(right_child) and is_planet(left_child):
        if len(right_b)>0 and len(left_b)==0:
            if size(right_child)>size(left_child):
                right_b.append(right_child)
                right_b.append(left_child)
                branches.append(right_b)
            else:
                right_b.append(left_child)
                right_b.append(right_child)
                branches.append(right_b)
        elif len(left_b)>0 and len(right_b)==0:
            if size(right_child)>size(left_child):
                left_b.append(right_child)
                left_b.append(left_child)
                branches.append(left_b)
            else:
                left_b.append(left_child)
                left_b.append(right_child)
                branches.append(left_b)



        else:
            branches.append(left_b)
            branches.append(right_b)
        left_b=[]
        right_b=[]

    return tree(root,branches)



def left_part(m):
    return m[1][2]
def right_part(m):
    return m[2][2]



def tree(root,branches=[]):
   print("tree()",[root]+list(branches))
   return [root]+list(branches)
def root(tree):
   #print(f"root tree={tree}")
   #print("root()",tree[0])
    x=type(tree)
    #print(f'type_root={x}')
    return tree[0]
def branches(tree):
    #print(f"branches tree={tree}")
    #x=type(tree)
    #print(f'type_root={x}')
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
#t, u, v = examples()
#print(t)
#print_tree(totals_tree(t))
#print_tree(totals_tree(u))
#print_tree(totals_tree(v))
###########################
# 6.0002 Problem Set 1a: Space Cows
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time


# ================================
# Part A: Transporting Space Cows
# ================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cows={}
    with open("ps1_cow_data.txt") as fil:
        for line in fil:
            #print(f"line={line}")
            cows[line[0:line.index(',')]]=line[line.index(',')+1]
            #print(cows)
    return cows


# Problem 2
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips

   # >>> cows={"Raj":6,"Billu":5,"Tambi":8,"Sankli":3,"More Sankli":1,"Avg":5,"Wataga":4}
    #>>> greedy_cow_transport(cows,10)
        [[Tambi,More Sankli],[Raj,Sankli],[Billu,Avg],[Wataga]]

    """
    # TODO: Your code here
    remaining=list(sorted(cows.values(),reverse=True))
    taken=[]
    cp_limit=limit


    #remaining.pop()
    #print(f'remaining={remaining}')
    rem_length=len(remaining)


    while rem_length>0:
        index=0
        temp=[]
        cp_limit=limit
        while cp_limit>0 and index<rem_length:
            if cp_limit-int(remaining[index])>=0:
                cp_limit-=int(remaining[index])
                temp.append(remaining[index])
                rem_length-=1
                remaining.remove(remaining[index])
            else:
                index+=1
        taken.append(temp)

    keys=list(cows.keys())
    tmp_list=[]
    final_list=[]

    #print("alu")
    for weight in taken:
        for ind_weight in weight:
            for name in keys:
                if cows[name] == ind_weight:
                    tmp_list.append(name)
                    keys.remove(name)
                    if len(tmp_list)==len(weight):
                        final_list.append(tmp_list)
                        tmp_list=[]
                    break
    return final_list








# Problem 3
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    best=[]
    makes_weight=True
    all_taken=False
    first=True #keep track of first partition that meets constraints so best can be set = to that
    num_taken = 0 #number of cows taken on trip

    for partition in get_partitions(list(cows.values())):
        makes_weight=True
        all_taken=False
        #print(f'partition={partition} ',end='')
        num_taken=0
        for subset in partition:
            #print(f'subset={subset}')
            if sum(subset)>limit:
                makes_weight=False
                break
            num_taken+=len(subset)
            #print(f'num_taken={num_taken}')
            if num_taken==len(cows):
                all_taken=True
        if first and makes_weight and all_taken:
            best = partition
            first = False
        #print(f"makes_weight={makes_weight} and all_taken={all_taken}")
        if makes_weight and all_taken:
            if len(partition)<len(best):
                #print(f'partition={partition}')
                best=partition
    #print(f'best={best}')

    #convert list of weights to list of names
    tmp_list=[]
    keys=list(cows.keys())
    final_list=[]

    for set in best:
        for ind_weight in set:
            for name in keys:
                if cows[name] == ind_weight:
                    tmp_list.append(name)
                    keys.remove(name)
                    if len(tmp_list)==len(set):
                        final_list.append(tmp_list)
                        tmp_list=[]
                    break
    return final_list

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    animals=load_cows("ps1_cow_data.txt")
    start=time.time()
    greed_list=greedy_cow_transport(animals,10)
    end=time.time()
    greed_time=end-start

    start = time.time()
    brute_list = greedy_cow_transport(animals, 10)
    end = time.time()
    brute_time = end - start

    print(f"Brute force found {brute_list} in {brute_time} seconds\nGreedy found {greed_list} in {greed_time} seconds for ps1_cow_data.txt")

    animals = load_cows("ps1_cow_data_2.txt")
    start = time.time()
    greed_list = greedy_cow_transport(animals, 10)
    end = time.time()
    greed_time = end - start

    start = time.time()
    brute_list = greedy_cow_transport(animals, 10)
    end = time.time()
    brute_time = end - start

    print(f"Brute force found {brute_list} in {brute_time} seconds\nGreedy found {greed_list} in {greed_time} seconds for ps1_cow_data_2.txt")

#cows={"Raj":6,"Billu":5,"Tambi":8,"Sankli":3,"More Sankli":1,"Avg":5,"Wataga":4}
#cows={"Raj":6,"Billu":5,"Tambi":8}
#print(greedy_cow_transport(cows,10))
#print("asjas")
compare_cow_transport_algorithms()
#print(brute_force_cow_transport(cows,10))

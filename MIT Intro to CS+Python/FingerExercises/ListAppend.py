#pg 98 finger exercise
L = [1,2,3]
L.append(L)
print(f"L is {L[-1]}")

L_bad_copy = L
L_bad_copy.remove(1)
print(f"L is {L}")

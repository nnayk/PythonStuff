import string
#finger exercise pg 117

#lines 4-7 i just wanted to look at the random ordering of sets, the actual finger exercise begins line 9
#letters = {"a","b","c"}

#for char in letters:
 #   print(char,end=" ")

def get_mind(d):
     letters = string.ascii_lowercase
     min_lett = 'z' #initially set min_lett to z so that earlier letters will be chosen
     #key = ''
     #val = ''
     for key, val in d.items():
        if letters.index(key) < letters.index(min_lett):
            min_lett = key
     return d[min_lett]

d = {'b' : 1, 'd' : 3, 'n' : 13, 'z' : 25, 'a': 0 }
early_index = get_mind(d)
print(f"The earliest index in this dictionary is {early_index}.")

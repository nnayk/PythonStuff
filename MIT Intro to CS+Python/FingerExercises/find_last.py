#pg 87 finger exercise 2
def findy(s, sub):
    s = s[::-1]
    sub = sub[::-1]
    return s.find(sub)
index = findy(sub="sub",s='subasasasub')

if index == -1:
    print(None)
else:
    print(index)

ab = "ab"
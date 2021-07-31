from operator import mul

#print(mul(9,2))
def search(f):
    x=0
    while True:
        if f(x):
            return x
        x+=1
def square(x):
    return x**2
def inverse(f):
    return lambda y: search(lambda x: f(x)==y)
print(inverse(square)(16))
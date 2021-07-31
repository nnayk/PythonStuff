def weird (x):
    global y
    x += ['b']
    print(y)
y=['a']
weird(y)
print(y)
first = {
    'a':1,'b':2
}

second = {
    'a':1,'b':2
}

#print(first==second)



# Python program to demonstrate
# working of keys()

# initializing dictionary
test_dict = { "geeks" : 7, "for" : 1, "gally" : 2 }

# accessing 2nd element using naive method
# using loop
j = 0
i=0
#the following 2 are the exact same
for i in test_dict.keys():
	print (f'{i} key using loop : '+str(i))
	j = j + 1

for i in test_dict:
	print (f'{i} key using loop : '+str(i))
	j = j + 1

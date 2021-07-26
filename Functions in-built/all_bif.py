# Check if all items in a list are True:

mylist = [True, True, True]
x = all(mylist)
print(x)

# Check if all items in a list are True:

mylist = [0, 1, 1]
x = all(mylist)
print(x)

# Check if all items in a tuple are True:

mytuple = (0, True, False)
x = all(mytuple)
print(x)

# Check if all items in a set are True:

myset = {0, 1, 0}
x = all(myset)
print(x)

# Check if all items in a dictionary are True:

mydict = {0 : "Apple", 1 : "Orange"}
x = all(mydict)
print(x)
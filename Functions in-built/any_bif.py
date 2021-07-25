# Check if any of the items in a list are True:

mylist = [False, True, False]
x = any(mylist)


# Check if any item in a tuple is True:

mytuple = (0, 1, False)
x = any(mytuple)


# Check if any item in a set is True:

myset = {0, 1, 0}
x = any(myset)


# Check if any item in a dictionary is True:

mydict = {0 : "Apple", 1 : "Orange"}
x = any(mydict)

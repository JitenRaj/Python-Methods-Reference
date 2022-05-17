"""The index() method finds the first occurrence of the specified value.

The index() method raises an exception if the value is not found."""


# Search for the first occurrence of the value 8, and return its position:

mytuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = mytuple.index(8)

print(x)
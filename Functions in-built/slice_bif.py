# Create a tuple and a slice object. Use the slice object to get only the two first items of the tuple:

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])

# Create a tuple and a slice object. Start the slice object at position 3, and slice to position 5, and return the result:

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])

# Create a tuple and a slice object. Use the step parameter to return every third item:

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])

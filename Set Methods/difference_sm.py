# Return a set that contains the items that only exist in set x, and not in set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)

# Reverse the first example. Return a set that contains the items that only exist in set y, and not in set x:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = y.difference(x)

print(z)
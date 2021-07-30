# Freeze the list, and make it unchangeable:

mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)

x[1] = "strawberry"

print(x)
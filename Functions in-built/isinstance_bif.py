# Check if the number 5 is an integer:

x = isinstance(5, int)

print(x)

# Check if "Hello" is one of the types described in the type parameter:

y = isinstance("Hello", (float, int, str, list, dict, tuple))

print(y)

# Check if y is an instance of myObj:

class myObj:
  name = "Jiten"

b = myObj()

a = isinstance(b, myObj)

print(x,y)

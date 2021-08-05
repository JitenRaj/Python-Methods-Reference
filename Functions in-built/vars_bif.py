# Return the __dict__ atribute of an object called Person:

class Person:
  name = "John"
  age = 36
  country = "norway"

x = vars(Person)

print(x)

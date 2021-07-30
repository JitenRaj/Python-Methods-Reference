# Check if the "Person" object has the "age" property:

class Person:
  name = "John"
  age = 36
  country = "Norway"

x = hasattr(Person, 'age')
print(x)
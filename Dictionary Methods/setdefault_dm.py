# Get the value of the "model" item:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)

# Get the value of the "color" item, 
# if the "color" item does not exist, 
# insert "color" with the value "white":

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)

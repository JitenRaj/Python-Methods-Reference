# Inside the placeholders we can add a formatting type to format the result

# Use "<" to left-align the value:
# :<5 , here 5 is used to set the available space for the value to 5 character
txt= "I have {:<5} books."
print(txt.format(10))

# Use ">" to right align the value :
# :>5 , here 5 is used to set the available space for the value to 5 character
txt1 = "I have {:>5} pens."
print(txt1.format(10))

# Use "^" to center align the value :
# :^5 , here 5 is used to set the available space for the value to 5 character
txt2 = "I have {:^5} pencils."
print(txt2.format(2))
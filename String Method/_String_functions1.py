# Strings formatting

# Price work as placeholder here and .2f convert number into float
# The placeholder can be identified using named indexes {price},
# numbered indexes {0}, or even empty placeholders {}

txt="For only {price:.2f} dollers!"
print(txt.format(price=49))

txt1="My name is {fname},I\'m {age}"
print(txt1.format(fname="Jiten",age=21))

txt2="My name is {0}, I\'m {1}"
print(txt2.format("Jiten",21))

txt3= "My name is {}, I\'m {}"
print(txt3.format("Jiten",21))
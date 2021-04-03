# User Defined Functions
# Returning from Functions

# Certain functions, such as int or str returns a value instead of outputting it
# the return function can not be used outside  of a function definition

# To check which number is maximum number among them
def max(x,y):      
    if x>=y:       # Here if compare x and y , and if x is greater of equal to y
        return x   # It returns x
    else:          # or else
        return y   # It returns y

print(max(4,7))
# Here x is not greater than or equal to  y
# so it return y according else block statement 
# answer will be 7 , 7>4

x=max(8,8)
# Here x is not greater but it is equal to y
# so it return x according if block statement 
# answer will be 8 , 8==8
print(x)

print(max(6,5))
# Here x is greater than y
# so it return x according if block statement 
# answer will be 6 , 6>5

###########################################################
print("\n")

# To check which number is minimum number among them

def min(x,y):
    if x<=y:
        return x
    else:
        return y

print(min(15,13))
y=min(14,14)
print(y)
print(min(17,19))
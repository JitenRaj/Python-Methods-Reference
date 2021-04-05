def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x
    
def lcm(x,y):
    lcm=(x*y)//gcd(x,y)
    return lcm

num1=54
num2=24

print("The L.C.M. of", num1,"and", num2,"is",lcm(num1,num2))
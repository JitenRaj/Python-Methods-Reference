def ComputeLCM(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    
    while(True):
        if((greater%x==0) and (greater%y==0)):
            lcm=greater
            break
        greater+=1

    return lcm

num1=54
num2=24

print("The H.C.F of", num1,"and", num2,"is",ComputeLCM(num1,num2))

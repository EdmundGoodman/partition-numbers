def f(x,y):
    if x==1 or x==0:
        return 1
    return sum([f(x-i,i) for i in range(1,min(x,y)+1)])

def g(x):
    return f(x,x)
    
targetNumber = int(input("Enter a number: "))
print("Final total: ",g(targetNumber))

def f_print(x,y,d=0):
    if x==1 or x==0:
        return 1
    total = 0
    for i in range(1,min(x,y)+1):

        #Print all the solutions
        onesString = "+"+"+".join(["1" for _ in range(x-i)]) if x-i else ""
        if d==0 or i!=1:
            print("{}{}{}".format("\t"*d,i,onesString))

        total += f(x-i,i,d+1)
    return total
    
def g(x):
    return f_print(x,x)

targetNumber = int(input("Enter a number: "))
print("Final total: ",g(targetNumber))

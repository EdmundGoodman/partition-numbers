import functools

#https://medium.com/@nkhaja/memoization-and-decorators-with-python-32f607439f84
d\ef memoize(func):
    cache = func.cache = {}

    @functools.wraps(func)
    def memoized_func(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return memoized_func

@memoize
def f(x,y):
    if x==1 or x==0:
        return 1
    return sum([f(x-i,i) for i in range(1,min(x,y)+1)])

def g(x):
    return f(x,x)

targetNumber = int(input("Enter a number: "))
print("Final total: ",g(targetNumber))

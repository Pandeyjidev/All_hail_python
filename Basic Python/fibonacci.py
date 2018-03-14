def F(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        return F(n-1) + F(n-2)

def fib():
    # print("here")
    a,b = 0,1
    while True:
        # print(a)
        yield a
        a,b = b, a+b
        # print(a)

# # print(F(5))
# fibo()
# F(3)
for index, fibonacci_number in zip(range(10), fib()):
     print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))
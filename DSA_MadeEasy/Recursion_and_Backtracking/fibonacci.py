def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a+b

# print(fibonacci(6))

for idx , fibo_num in zip(range(10),fibonacci2()):
    print('{i:3}: {f:3}'.format(i=idx,f=fibo_num))
# Sieve of Eratosthenes
def CountPrimes(n):
    if n <=2: 
        return 0
    prime = [True for i in range(n)]
    prime[0] = prime[1] = False
    p = 2
    while(p*p <=n):
        if prime[p] == True:
            for i in range(2*p, n, p):
                prime[i] = False
        p += 1
    return sum(prime)
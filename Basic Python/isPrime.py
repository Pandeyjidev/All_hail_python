import math
def isPrime(num):
# Returns True if num is a prime number, otherwise False.
# Note: Generally, isPrime() is slower than primeSieve().
# all numbers less than 2 are not prime
    if num < 2:
        return False
        # see if num is divisible by any number up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
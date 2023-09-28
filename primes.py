"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isprime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if(n%i ==0):
            return False
    return True

def primes(number_of_primes):
    if number_of_primes <=0:
        raise ValueError("Positive number required")
    primelist = []
    i = 2
    while len(primelist) < number_of_primes:
        if isprime(i):
            primelist.append(i)
        i+=1
    return list

#test



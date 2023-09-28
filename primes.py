"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def checkprime(n):
    if n <= 1:
        return False
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError('enter a positive number')
    listOfPrimes = []
    i = 2
    while len(listOfPrimes) < number_of_primes:
        if checkprime(i):
            listOfPrimes.append(i)
        i += 1
    return listOfPrimes

#test

print(primes(5))


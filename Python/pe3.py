import random
import math
import sys

"""
!headerdoc!

Sieve of Eratosthenes

@param n The number to decompose

@return List of prime factors of n

"""
def sieve_of_eratosthenes(n):
    prime_factors = [2]
    i = 3
    while i < int(math.sqrt(n)) + 1:
        if n % i == 0 and is_prime(i):
            prime_factors.append(i)
        i += 2
    return(prime_factors)


def is_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    if n in primes:
        return True
    for num in primes:
        if n % num == 0:
            return False
        else:
            i = 9
            while i < int(math.sqrt(n))+1:
                if n % i == 0:
                    return False
                i += 2
    return True


if __name__ == "__main__":
    print(sieve_of_eratosthenes(int(sys.argv[1])))

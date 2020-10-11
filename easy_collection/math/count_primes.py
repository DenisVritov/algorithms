"""
Count the number of prime numbers less than a non-negative number, n.

Note:
    0 <= n <= 5 * 10**6

Input: n=10
Output: 4
"""

from typing import *
import math


def count_primes(n: int) -> int:
    """
    Primality test: Divide number by all primes that come before it, if divisible by at least one then not prime.
                    Can optimize by only testing primes up to sqrt(x) where x is being tested for primality.

    Brute force: Test all the numbers up to n for primality. Create a bit array of length n and mark 1 if prime
                 and 0 if not prime.

    Better solution: Rather than constantly testing whether x is divisible by a prime, simply mark all multiples of 2
                     as non-prime. For prime p mark off all multiples of p starting with p**2 because any multiple of p
                     less than p**2 will have been marked off as a multiple of the value b where b<p. Can terminate at
                     once p > sqrt(n) because all multiples between sqrt(n) and n will have already been marked off.
    """

    if n < 3:
        return 0

    primes = [True] * (n+1)
    primes[0] = False
    primes[1] = False
    primes[n] = False

    for i in range(2, math.ceil(math.sqrt(n))):
        if primes[i]:
            j = i*i
            while j < n:
                primes[j] = False
                j = j+i

    return sum(primes)
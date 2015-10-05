#!/usr/bin/python3
# gcd is in the fractions module
# so to use:
# from fractions import gcd
# gcd(20, 8)
# 4

def is_prime(n):
    """Returns True if n is prime"""
    if n < 2: return False
    if n == 2: return True
    if n == 3: return True
    if n % 2 == 0: return False
    if n % 3 == 0: return False

    i = 5
    w = 2
    while i * i <= n:
        print(i, w)
        if n % i == 0: 
            return False

        i += w
        w = 6 - w

    return True

def largest_prime_factor(n):
    """Returns the largest prime factor of n"""
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

def prime_factors(n):
    """Returns all prime factors of n"""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    return factors

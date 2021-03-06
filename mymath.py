"""This module implements a variety of math functions not found in the standard
library. Most of them are related to prime numbers and divisors"""

# note that gcd is in the fractions module
# so to use:
# from fractions import gcd
# gcd(20, 8)
# 4

def is_prime(number):
    """Returns True if number is prime"""
    if number < 2:
        return False
    if number == 2:
        return True
    if number == 3:
        return True
    if number % 2 == 0:
        return False
    if number % 3 == 0:
        return False

    # all primes are of the form 6k +- 1, so we iterate through that list
    i = 5
    constant = 2
    while i * i <= number:
        if number % i == 0:
            return False

        i += constant
        constant = 6 - constant

    return True

def largest_prime_factor(number):
    """Returns the largest prime factor of number"""
    if number < 2:
        raise ValueError("A value less than 2 was passed in")
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
    return number

def prime_factors(number):
    """Returns all prime factors of number"""
    i = 2
    factors = []
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    return factors

def proper_divisors(number):
    """Returns all proper divisors of number"""
    divisors = [1]
    temp = [d for d in range(2, number//2+1) if number % d == 0]
    divisors += temp
    return divisors

def is_amicable(num_a, num_b):
    """Returns True if num_a and num_b are amicable numbers"""
    if num_a == num_b:
        return False
    a_divisors = proper_divisors(num_a)
    b_divisors = proper_divisors(num_b)
    return (sum(a_divisors) == num_b) and (sum(b_divisors) == num_a)

from nose.tools import *
from euler.mymath import *

def test_first_100_non_primes_is_prime_():
    non_primes = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25,
    26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50,
    51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75,
    76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 
    99, 100, 102, 104, 105, 106, 108, 110, 111, 112, 114, 115, 116, 117, 118, 
    119, 120, 121, 122, 123, 124, 125, 126, 128, 129, 130]
    for non_prime in non_primes:
        assert is_prime(non_prime) == False

def test_first_100_primes_is_prime_():
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,
    89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,
    191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,
    293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,
    419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,
    541]
    for prime in primes:
        assert is_prime(prime) == True

def test_invalid_values_largest_prime_factor():
   assert_raises(ValueError, largest_prime_factor, -4)
   assert_raises(ValueError, largest_prime_factor, -3)
   assert_raises(ValueError, largest_prime_factor, -2)
   assert_raises(ValueError, largest_prime_factor, -1)
   assert_raises(ValueError, largest_prime_factor, 0)
   assert_raises(ValueError, largest_prime_factor, 1)

def test_first_100_largest_prime_factor():
    factors = [2, 3, 2, 5, 3, 7, 2, 3, 5, 11, 3, 13, 7, 5, 2, 17, 3, 19, 5, 7,
    11, 23, 3, 5, 13, 3, 7, 29, 5, 31, 2, 11, 17, 7, 3, 37, 19, 13, 5, 41, 7,
    43, 11, 5, 23, 47, 3, 7, 5, 17, 13, 53, 3, 11, 7, 19, 29, 59, 5, 61, 31, 7,
    2, 13, 11, 67, 17, 23, 7, 71, 3, 73, 37, 5, 19, 11, 13, 79, 5, 3, 41, 83, 7,
    17, 43, 29, 11, 89, 5, 13, 23, 31, 47, 19, 3, 97, 7, 11, 5]
    for i, factor in enumerate(factors):
        assert largest_prime_factor(i + 2) == factor

def test_proper_divisors():
    assert proper_divisors(4) == [1, 2] 
    assert proper_divisors(6) == [1, 2, 3]
    assert proper_divisors(8) == [1, 2, 4]
    assert proper_divisors(10) == [1, 2, 5]
    assert proper_divisors(12) == [1, 2, 3, 4, 6]
    assert proper_divisors(14) == [1, 2, 7]
    assert proper_divisors(15) == [1, 3, 5]
    assert proper_divisors(16) == [1, 2, 4, 8]
    assert proper_divisors(18) == [1, 2, 3, 6, 9]
    assert proper_divisors(20) == [1, 2, 4, 5, 10]

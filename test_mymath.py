from euler.mymath import is_prime

def test_is_prime_corner_cases():
    assert is_prime(0) == False
    assert is_prime(1) == False 
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False

def test_is_prime_first_100_primes():
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,
    89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,
    191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,
    293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,
    419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,
    541]
    for prime in primes:
        assert is_prime(prime) == True



# -*- coding: utf-8 -*-
"""
Created on Thu Nov 01 14:42:54 2012

@author: n3wp0llut10n
"""

from numpy import *

#using this instead of num = sum(range(1,i+1)) is over 10x faster
def triangle(n):
    return n*(n+1)/2
    
#factor a number into all of its unique factors
def factor_uniques(n):
    if n == 1: return [1]
    ret = [1]
    i = 2
    limit = n**0.5
    while i <= limit:
        if n % i == 0:
            j = n / i
            ret.append(i)
            if i != j:
                ret.append(j)
        i += 1
        
    if len(ret) == 1:
        ret.append(n)
    return ret

#factor a number into its prime factors
def factor_primes(n):
    if n == 1: return [1]
    i = 2
    limit = n**0.5
    while i <= limit:
        if n % i == 0:
            ret = factor_primes(n/i)
            ret.append(i)
            return ret
        i += 1
    return [n]

#generate a list of primes
def generate_primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

i = 1
my_factors = [1]
while(len(my_factors) < 500):
    my_triangle = triangle(i)
    my_factors = factor_uniques(my_triangle)
    i += 1

print(i)
print(my_triangle)
print(len(my_factors))

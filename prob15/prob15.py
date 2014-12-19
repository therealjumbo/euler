import math

def triangle_row(j):
    return (j*2)
    
def coefficient_index(n):
    return (n/2)
    
def calculate_binomial_coefficient(n, k):
    return (math.factorial(n) / math.factorial(k) / math.factorial(n - k))
    

grid_side = 20

n = triangle_row(grid_side)
print(n)
k = coefficient_index(n)
print(k)
binomial_coefficient = calculate_binomial_coefficient(n, k)
print (binomial_coefficient)

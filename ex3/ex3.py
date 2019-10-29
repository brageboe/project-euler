import gmpy2
from numpy import prod

prime_master = 600851475143
prime_current = prime_master
p = 2 # the first potential prime factor
prime_factors = []

while prod(prime_factors) != prime_master:
    if prime_current % p == 0: # if p is a prime factor of prime_current
        prime_factors.append(p) # add to list of prime factors
        prime_current = prime_current / p # update prime_current
    else:
        p = int(gmpy2.next_prime(p))

print(prime_factors)

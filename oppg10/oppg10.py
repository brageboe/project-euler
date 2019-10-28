from gmpy2 import next_prime

n = 0
N = 2000 * 1000 # 2e6
sum_primes = 0

while n < N:
    sum_primes += n
    n = int(next_prime(n)) 

import gmpy2

goal_prime = 10001
current_prime = x = 0

while current_prime != goal_prime:
    x = gmpy2.next_prime(x)
    current_prime += 1

print(x)

# alternatively:
#import sympy; sympy.prime(10001)

from math import sqrt

for b in range(1,500):
    for a in range (1,b):
        c = sqrt(a**2 + b**2)
        if c % 1 == 0:  # c must be integer, check for remainders of 1
            c = int(c)  # convert from floating to int
            if a + b + c == 1000:
                print("a = ", a, ", b = ", b, ", c = ", c)
                print("abc = ", a*b*c)
                break

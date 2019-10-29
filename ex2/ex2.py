def sum_fib_even(fib_seq):
    # return the sum of even numbers of a Fibonacci sequence
    sum = 0
    for i in fib_seq:
        if i % 2 == 0:
            sum += i
    return sum

def fib_recursive(n): # return the nth number in the Fibonacci sequence
    if n < 0:
        raise ValueError("N must be a non-negative integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def fib(N):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < N:
        result.append(a)
        a, b = b, a+b
    return result

if __name__ == '__main__':
    N = 4000 * 1000
    print(sum_fib_even(fib(N)))
    # SUPER SLOW METHOD:
    #fiblist = []
    #for i in range(1,N):
    #    fiblist.append(fib_recursive(i))
    #print(sum_fib_even(fiblist))

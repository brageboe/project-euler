square_of_sum = sum(range(101))**2
sum_pwr = 0
for i in range(101):
    sum_pwr += i**2
print(square_of_sum - sum_pwr)

# or equivalently:
print(sum(range(101)) ** 2 - sum(i ** 2 for i in range(101)))

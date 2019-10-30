def division_MYATTEMPT(division_success, number, criteria):
    while division_success < criteria:
        for i in range(1,20):
            if number % i == 0:
                division_success += 1
            else:
                number += 20
                division_success = 0
    return number

if __name__ == '__main__':
    criteria = 20
    number = 2520  # known smallest evenly divisible number by 1-10, our starting point
    division_success = 0
    print(division_MYATTEMPT(division_success, number, criteria))


# Someone's solution from the problem 5 forum:
def division_criteria(number, criteria):
    if criteria > 0:
        if number % criteria == 0:
            if division_criteria(number, criteria - 1):
                return True
            else:
                return False
        else:
            return False
    else:
        return True

if __name__ == '__PLACEHOLDER__':
    CRITERIA = 20
    smallest_multiple = 2520
    while not division_criteria(smallest_multiple, CRITERIA):
        smallest_multiple += 20
    print(smallest_multiple)

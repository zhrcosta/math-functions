def factorial(num):

    count = num
    value = num

    while count > 1:
        count -= 1
        value = value * count

    return value


print(factorial(5))

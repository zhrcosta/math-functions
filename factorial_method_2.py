def factorial(num):

    value = 1

    for n in range(value, num+1):
        value = value * n

    return value


print(factorial(7))

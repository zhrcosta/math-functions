"""
    Função para decompor um número inteiro em fatores primos,
    retornando uma lista
"""


def primeFac(num):

    def isprime(prime):

        divisors = 0

        for i in range(1, (prime//2)+1):
            if prime % i == 0:
                divisors += 1

        divisors += 1

        value = True if divisors == 2 else False
        print(value)

        return value

    fac = []
    val = num
    divisor = 2

    while val > 1:

        if isprime(divisor):
            if val % divisor == 0:
                val = val // divisor
                fac.append(divisor)
        else:
            divisor += 1
            print(divisor)

    return fac


print(primeFac(72))

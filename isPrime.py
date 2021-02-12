"""
    Função para testar se um número inteiro é primo ou não.
    Retorna um valor booleano
"""


def isprime(num):

    divisors = 0

    for i in range(1, (num//2)+1):
        if num % i == 0:
            divisors += 1

    divisors += 1

    value = True if divisors == 2 else False

    return value


print(isprime(19))

"""
    Função para testar se um número inteiro é primo ou não.
    Retorna um valor booleano
"""


def isprime(num):

    divisors = []
    d = 0
    b = None

    for i in range(1, (num//2)+1):
        if num % i == 0:
            divisors.append(i)
            d += 1

    divisors.append(num)
    d += 1

    if d == 2:
        b = True
    else:
        b = False

    return divisors, d, b


divs, amount, value = isprime(23)

print(divs)
print(amount)
print(value)

"""
    Função para multiplicar todos os valores de uma lista
"""


def multiply(*args):
    res = 1

    for value in args:
        res = res * value

    return res


print(multiply(2, 2, 2, 2, 3, 3))

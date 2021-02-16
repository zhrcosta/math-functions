"""
    Função que retorna o maior número par de uma lista
"""


def maxEvenNumber(list):

    max = 0

    for value in list:

        if value % 2 == 0 and value >= max:
            max = value

        else:
            continue

    return max


list_numbers = [0, 2, 5, 4, 5, 22, 23, 6]

print(maxEvenNumber(list_numbers))

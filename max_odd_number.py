"""
    Função que retorna o maior número impar
"""


def maxOddNumber(list):

    max = list[0]

    for value in list:

        if value % 2 >= 1 and value >= max:
            max = value
        else:
            continue

    return max


list_numbers = [3, 9, 2, 6, 11, 128, 23, 58, 29]

print(maxOddNumber(list_numbers))

"""
    Função que retorna o menor número par de uma lista
"""


def minEvenNumber(list):

    min = list[0]

    for value in list:

        if value % 2 == 0 and value <= min:
            min = value
            
        else:
            continue

    return min


list_numbers = [9, 2, 5, 4, 5, 22, 6, -2, -38]

print(minEvenNumber(list_numbers))

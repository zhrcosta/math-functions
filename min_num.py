'''
    Função para retornar o menor valor de uma lista
'''


def minNum(list):

    min = 0

    for value in list:

        if value <= min:
            min = value

    return min


list_numbers = [0, 2, 5, 4, 5, 22, -3, 6]

print(minNum(list_numbers))

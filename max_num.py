'''
    Função para retornar o valor maximo de uma lista
'''


def maxNum(list):
    max = list[0]

    for value in list:
        if value >= max:
            max = value

    return max


list_numbers = [0, 2, 5, 4, 5, 22, 22.1, 6]

print(maxNum(list_numbers))

'''
    Função para retornar o maior valor de uma lista
'''


def maxNum(list):
    max = list[0]

    for value in list:
        if value >= max:
            max = value

    return max


list_numbers = [0, 2, 5, 4, 5, 22, 23, 6]

print(maxNum(list_numbers))

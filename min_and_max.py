

def minMax(list):

    # Função que retorna dois valores de uma lista ao mesmo tempo.
    # O maior e o menor valor de uma lista.

    min = list[0]
    max = list[0]

    for value in list:

        if value <= min:
            min = value

        if value >= max:
            max = value

    return min, max


list_numbers_1 = [2, 5, 32, 1, 0, 2, 3, 55, 4, 11]
list_numbers_2 = [2, 5, 32, 1, 0, 2, -3, 55, 4, 11]


min_value_1, max_value_1 = minMax(list_numbers_1)
min_value_2, max_value_2 = minMax(list_numbers_2)

print("Lista 1")
print("Menor valor: {}".format(min_value_1))
print("Maior valor: {}".format(max_value_1))

print("\n")

print("Lista 2")
print("Menor valor: {}".format(min_value_2))
print("Maior valor: {}".format(max_value_2))

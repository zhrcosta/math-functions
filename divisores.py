def divisores(num):

    # lista para armazenar os divisores
    divisors = []

    """Nesse laço os divisores são testados até a metade + 1 do numero informado, evitando loops desnecessários, ja que não 
    existe divisor para um numero maior que a metade dele mesmo
    Ex: 72/2 = 36, não terá um divisor maior que 36 para o 72.
    """
    for i in range(1, (num//2)+1):
        if num % i == 0:
            divisors.append(i)

    # Adiciona a lista dos divisores o próprio número.
    divisors.append(num)
    return divisors


print(divisores(72))
print()
print(len(divisores(72)))

"""
    Função para testar se um número inteiro é primo ou não.
    Retorna um valor booleano
"""


def isprime(num):

    # Variavel para registar o incremento de quantos divisores o laço FOR irá adicionar
    divisors = 0

    #Teste de divisão para cada número até a metade de NUM
    for i in range(1, (num//2)+1):
        if num % i == 0:
            divisors += 1

    # No final do laço é adicionado mais um divisor reverente ao valor adicionado na variavel NUM
    divisors += 1

    # Se houver apenas 2 divisores o número é Primo, atribuindo True
    value = True if divisors == 2 else False

    return value


print(isprime(23))

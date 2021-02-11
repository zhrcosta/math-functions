def divisores(num):
    divs = []
    for i in range(1, (num//2)+1):
        if num % i == 0:
            divs.append(i)
    divs.append(num)
    return divs


print(divisores(72))

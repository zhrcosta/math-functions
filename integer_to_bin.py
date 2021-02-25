

def intToBin(num):

    dividendo = num
    str_bim = ""
    quociente = 0

    while not dividendo <= 1:

        resto = dividendo % 2
        quociente = dividendo // 2
        dividendo = quociente
        str_bim = str(resto) + str_bim

    else:
        str_bim = str(quociente) + str_bim

    return str_bim


print(intToBin(33))

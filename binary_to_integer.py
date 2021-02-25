

def binToInt(string):

    string = string[::-1]
    integer = 0

    for exp in range(len(string)):
        if string[exp] == "1":
            integer += 2**exp

    return integer


print(binToInt("100001"))

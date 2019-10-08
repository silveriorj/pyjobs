def retornaPrimo():
    num = int(input("Digite um numero maior que 1: "))

    f = 2 # fator
    saida = str(num)+" = "
    while num != 1:
        # conta a multiplicidade de fator em num
        mult = 0
        while num%f == 0:
            num = num / f
            mult += 1

        # imprime a multiplicade do fator
        if mult != 0:
            saida += (str(f)+"x")*mult

        f += 1
    print(saida)

retornaPrimo()
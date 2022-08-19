t = int(input(''))  # N de testes

testes = []

for i in range(0, t):
    n = int(input('')) # Cada teste
    testes.append(n)


resultados = []

for teste in testes:
    if teste == 1:
        resultados.append(2)
    elif teste == 3:
        resultados.append(1)

    elif teste % 2 == 0:
        if teste == 6:
            resultados.append(2)
        else:
            if teste < 6:
                resultados.append(2)
            elif teste > 6:
                for i in range(0, teste):
                    if teste == 2 or teste == 4:
                        teste -= 2

                    elif teste == 0:
                        resultados.append(i)
                        break
                    teste -= 3

    elif teste % 2 == 1:
        for i in range(0, teste):
            if teste == 2:
                teste -= 2

            elif teste == 0:
                resultados.append(i)

            teste -= 3


for resultado in resultados:
    print(resultado)
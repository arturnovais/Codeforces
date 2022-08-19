# 2-3 Moves

t = int(input(''))  # N de testes

testes = []

for i in range(0, t):
    n = int(input(''))  # Cada teste
    testes.append(n)

resultados = []

for teste in testes:
    if teste == 1 or teste == 4:
        resultados.append(2)
    elif teste == 2 or teste == 3:
        resultados.append(1)

    elif teste % 3 == 0:
        resultados.append(teste / 3)

    elif teste % 3 == 1:
        teste -= 4
        resultados.append((teste / 3) + 2)

    elif teste % 3 == 2:
        resultados.append((teste / 3) + 1)

for resultado in resultados:
    print(int(resultado))

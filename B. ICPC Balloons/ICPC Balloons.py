t = int(input(''))

pontuacao = []

for i in range(0, t):
    problemas = []
    pontos = 0

    n = int(input(''))
    s = str(input(''))

    for letra in s:
        if letra not in problemas:
            pontos += 2

        else:
            pontos += 1

        problemas.append(letra)
    pontuacao.append(pontos)

for ponto in pontuacao:
    print(ponto)

"Exercicio 3"
from math import inf

value = []
total = 0
for indice in range(20):
    value.append(float(input("Digite um número:")))

while indice < len(value):
    total += value[indice]
    indice += 1

media = total/len(value)

print("A média é de:",media)

MaiorValor = -inf
indice = 0
while indice < len(value):
    if value[indice] > MaiorValor:
        MaiorValor = value[indice]

    indice = indice + 1

print("O maior valor é:",MaiorValor)

MenorValor = +inf
indice = 0

while indice < len(value):
    if value[indice] < MenorValor:
        MenorValor = value[indice]

    indice = indice + 1

print("O menor valor da lista é:",MenorValor)


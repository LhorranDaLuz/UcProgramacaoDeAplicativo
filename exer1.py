"Exercicio 1"
from math import inf

"A)"

l = [5, 7, 2, 9, 4, 1, 3]
count = 0
for numero in range(len(l)):
    count = count + 1

print(f"O tamanho da lista é:{count}")

"B)"

MaiorValor = -inf
indice = 0

while indice < len(l):
    if l[indice] > MaiorValor:
        MaiorValor = l[indice]

    indice = indice + 1

print("O maior valor da lista é:",MaiorValor)

"C)"

MenorValor = +inf
indice = 0

while indice < len(l):
    if l[indice] < MenorValor:
        MenorValor = l[indice]

    indice = indice + 1

print("O menor valor da lista é:",MenorValor)

"D)"

indice = 0
total = 0

while indice < len(l):
    total = total + l[indice]
    indice = indice + 1

print("A soma dos valores da lista é:",total)

"E)"

for indice1 in range(len(l)):
    for indice2 in range(len(l)):
        if l[indice1] < l[indice2]:

            vtemp = l[indice1]
            l[indice1] = l[indice2]
            l[indice2] = vtemp

print("A lista em ordem crescente é:",l)

"F)"

for indice1 in range(len(l)):
    for indice2 in range(len(l)):
        if l[indice1] > l[indice2]:

            vtemp = l[indice1]
            l[indice1] = l[indice2]
            l[indice2] = vtemp

print("A lista em ordem decrescente é:",l)






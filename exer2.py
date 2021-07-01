"Exercicio 2"

value = []
total = 0
for indice in range (4):
    value.append(int(input("Digite um número:")))

while indice < len(value):
    total += value[indice]
    indice += 1

media = total/len(value)

if media < 1:
    print("Negativo!")

else:
    print("Positivo!")


print(total)
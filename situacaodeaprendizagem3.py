#situação de aprendizagem 3
print(" =====================================================")
print("========== BEM VINDO A CALCULADORA DE TROCOS ==========")
print(" =====================================================")
print('')
valortotal = float(input("Informe o valor da compra:"))
print('')
valorpago = float(input("Informe o valor recebido pelo cliente:"))
print('')

vt = valortotal
vp = valorpago


troco = vp-vt

print("O troco do cliente é: R$", troco)


notas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05]


def otimizacao(troco, notas):
    unidadenotas = []

    for i in range(len(notas)):
        contador = 0

        while troco >= notas[i]:
            contador += 1
            troco -= notas[i]

        unidadenotas.append(contador)

    return troco, unidadenotas


troco, notasnecessarias = otimizacao(troco, notas)
troco, moedasnecessarias = otimizacao(troco, moedas)

for i in range(len(notas)):
    if notasnecessarias[i] > 0:
        print(notasnecessarias[i], "Notas de: R$", notas[i])

for i in range(len(moedas)):
    if moedasnecessarias[i] > 0:
        print(moedasnecessarias[i], "Moedas de: R$", moedas[i])
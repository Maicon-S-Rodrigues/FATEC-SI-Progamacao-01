def calcularMaiorValor(valorA, valorB):
    if valorA > valorB:
        return valorA
    return valorB

def calcularMenorValor(valorA, valorB):
    if valorA < valorB:
        return valorA
    return valorB

def calcularMedia(valorA, valorB):
    return (valorA + valorB) / 2

#---------------------------------------------------------------------------------------

valorA = int(input("Informe o primeiro valor: "))
valorB = int(input("Informe o segundo valor: "))

print("O Maior valor é ", calcularMaiorValor(valorA, valorB))
print("O Menor valor é ", calcularMenorValor(valorA, valorB))
print("A Média dos valores é ", calcularMedia(valorA, valorB))
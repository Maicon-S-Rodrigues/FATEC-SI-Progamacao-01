valor = float(input('Informe o Valor do produto: '))
importado = input('Este Produto é importado?\n( S )-> Sim  || ( N )-> Não)\n')

if(importado.upper() == "S") :
    valor = valor + (valor * 10) / 100
    print("Valor do produto Nacional: " , valor)

elif(importado.upper() == "N") :
    valor = valor + (valor * 5) / 100
    print("Valor do produto Nacional: " , valor)
else :
    print("Opção Invalida!")

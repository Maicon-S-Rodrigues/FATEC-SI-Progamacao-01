consumo = float(input("Informe a quantidade de MBytes consumidos pelo Cliente: "))
plano = float(input("Informe o Plano contratado pelo Cliente:\n[ 1 ]--> Ouro\n[ 2 ]--> Prata\n[ 3 ]--> Bronze\n"))

if plano == 1:
    valor = (0.30 * consumo) + 50
    print("O Valor a ser cobrado do Cliente 'Ouro' é de: R$ %2.f" % valor)

elif plano == 2:
    valor = (0.50 * consumo) + 30
    print("O Valor a ser cobrado do Cliente 'Prata' é de: R$ %2.f" % valor)
    
elif plano == 3:
    valor = (0.80 * consumo) + 20
    print("O Valor a ser cobrado do Cliente 'Bronze' é de: R$ %2.f" % valor)
    
else:
    print("Plano inválido!")
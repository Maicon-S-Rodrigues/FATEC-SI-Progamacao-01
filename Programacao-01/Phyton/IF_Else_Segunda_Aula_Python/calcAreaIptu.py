area = float(input("Informe a Area do Imóvel: "))
tipo = float(input("Informe o Tipo do Imóvel:\n[ 1 ]--> Residêncial\n[ 2 ]--> Comercial\n[ 3 ]--> Industrial\n"))

if tipo == 1:
    valor = area * 2
    print("O Valor do Imóvel é de: R$ %2.f" % valor)

elif tipo == 2:
    valor = area * 3
    print("O Valor do Imóvel é de: R$ %2.f" % valor)
    
elif tipo == 3:
    valor = area * 4
    print("O Valor do Imóvel é de: R$ %2.f" % valor)
    
else:
    print("Tipo de imóvel inválido!")
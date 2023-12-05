quantidadeResidencial = 0
quantidadeComercial = 0
quantidadeIndustrial = 0

valorTotalContasResidencial = 0
valorTotalContasComercial = 0
valorTotalContasIndustrial = 0
valorTotalSomado = 0

contador = 1
consumo = 0
conta = 0

while contador <= 5:
    conta = 0
    consumo = float(input(f"Informe o consumo do {contador}º Consumidor: "))
    tipoConsumidor = int(input(f"Informe o tipo do {contador}º consumidor:\n[1]-> Residencial\n[2]-> Comercial\n[3]-> Industrial\nEscolha:"))
    
    if tipoConsumidor == 1:
        quantidadeResidencial = quantidadeResidencial + 1
        conta = consumo * 0.3
        valorTotalContasResidencial = valorTotalContasResidencial + conta
    
    elif tipoConsumidor == 2:
        quantidadeComercial = quantidadeComercial + 1
        conta = consumo * 0.5
        valorTotalContasComercial = valorTotalContasComercial + conta
    
    elif tipoConsumidor == 3:
        quantidadeIndustrial = quantidadeIndustrial + 1
        conta = consumo * 0.7
        valorTotalContasIndustrial = valorTotalContasIndustrial + conta
        
    contador = contador + 1
        
valorTotalSomado = valorTotalContasResidencial + valorTotalContasComercial + valorTotalContasIndustrial
        
print("----------------------------------------------------------------------------------------")        
print("Quantidade de consumidores Residenciais: " , quantidadeResidencial)
print("Quantidade de consumidores Comerciais: " , quantidadeComercial)
print("Quantidade de consumidores Industriais: " , quantidadeIndustrial)
print("----------------------------------------------------------------------------------------")
print("Valor Total de consumidores Residenciais: R$ %2.f" % valorTotalContasResidencial)
print("Valor Total de consumidores Comerciais: R$ %2.f" % valorTotalContasComercial)  
print("Valor Total de consumidores Industriais: R$ %2.f" % valorTotalContasIndustrial)
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print("Valor Total Geral: R$ %2.f" % valorTotalSomado)


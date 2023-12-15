quantidade = 0
veiculosGasolina = 0
veiculosFlex = 0
veiculosDiesel = 0
totalGasolina = 0
totalFlex = 0
totalDiesel = 0
valorTotal = 0
continuar = 1

def calcularIpva(tipoVeiculo, valorDoVeiculo):
  ipva = 0
  
  if tipoVeiculo == 1:
    ipva = valorDoVeiculo * 0.04
  
  elif tipoVeiculo == 2:
    ipva = valorDoVeiculo * 0.03
    
  elif tipoVeiculo == 3:
    ipva = valorDoVeiculo * 0.02
    
  return ipva

#---------------------------------------------------------------------------------------->>>>

while continuar == 1:
  
  contador = 1
  
  tipoVeiculo = int(input(f"Informe o tipo de combustível do Veículo:\n[1]-> Gasolina\n[2]-> Flex/Álcool\n[3]-> Diesel\nEscolha:")) 
  quantidade = int(input(f"Informe a quantidade de Veículos deste tipo de combustível: "))
  
  if tipoVeiculo == 1:
    while contador <= quantidade:
      valorDoVeiculo = float(input(f"Informe o valor do {contador}º Veículo: "))
      veiculosGasolina = veiculosGasolina + 1
      totalGasolina = totalGasolina + calcularIpva(tipoVeiculo, valorDoVeiculo)
      contador = contador + 1
  
  elif tipoVeiculo == 2:
    while contador <= quantidade:
      valorDoVeiculo = float(input(f"Informe o valor do {contador}º Veículo: "))
      veiculosFlex = veiculosFlex + 1
      totalFlex = totalFlex + calcularIpva(tipoVeiculo, valorDoVeiculo)
      contador = contador + 1
  
  elif tipoVeiculo == 3:
    while contador <= quantidade:
      valorDoVeiculo = float(input(f"Informe o valor do {contador}º Veículo: "))
      veiculosDiesel = veiculosDiesel + 1
      totalDiesel = totalDiesel + calcularIpva(tipoVeiculo, valorDoVeiculo)
      contador = contador + 1
      
  continuar = int(input("Deseja adicionar mais Veículos ao cálculo?\n[1]-> Sim\n[2]-> Não\nEscolha:"))
  
valorTotal = totalGasolina + totalFlex + totalDiesel

print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")        
print("Quantidade de Veículos a Gasolina: " , veiculosGasolina)
print("Quantidade de Veículos Flex/Álcool: " , veiculosFlex)
print("Quantidade de Veículos a Diesel: " , veiculosDiesel)
print("----------------------------------------------------------------------------------------")
print("Valor Total do IPVA a ser pago para Veículos a Gasolina: R$ %2.f" % totalGasolina)
print("Valor Total do IPVA a ser pago para Veículos Flex/Álcool: R$ %2.f" % totalFlex)  
print("Valor Total do IPVA a ser pago para Veículos a Diesel: R$ %2.f" % totalDiesel)
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print("Valor Total a ser pago em IPVA: R$ %2.f" % valorTotal)
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
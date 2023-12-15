quantidade = 0
quantidadeCerveja = 0
quantidadeRefrigerante = 0
quantidadeAlimento = 0
totalCerveja = 0
totalRefrigerante = 0
totalAlimento = 0
valorTotal = 0
continuar = 1

while continuar == 1:
  
  contador = 1
  
  tipoProduto = int(input(f"Informe o tipo do produto:\n[1]-> Cerveja\n[2]-> Refrigerante\n[3]-> Alimento\nEscolha:")) 
  quantidade = int(input(f"Informe a quantidade que deseja desse Produto: "))
  
  if tipoProduto == 1:
    while contador <= quantidade:
      valorPago = float(input(f"Informe o valor que pagou no {contador}º Produto: "))
      totalCerveja = totalCerveja + valorPago
      quantidadeCerveja = quantidadeCerveja + 1
      contador = contador + 1
  
  elif tipoProduto == 2:
    while contador <= quantidade:
      valorPago = float(input(f"Informe o valor que pagou no {contador}º Produto: "))
      totalRefrigerante = totalRefrigerante + valorPago
      quantidadeRefrigerante = quantidadeRefrigerante + 1
      contador = contador + 1
  
  elif tipoProduto == 3:
    while contador <= quantidade:
      valorPago = float(input(f"Informe o valor que pagou no {contador}º Produto: "))
      totalAlimento = totalAlimento + valorPago
      quantidadeAlimento = quantidadeAlimento + 1
      contador = contador + 1
      
  continuar = int(input("Deseja adicionar mais Produtos?\n[1]-> Sim\n[2]-> Não\nEscolha:"))
  
valorTotal = totalCerveja + totalRefrigerante + totalAlimento

print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")        
print("Quantidade de Cervejas compradas: " , quantidadeCerveja)
print("Quantidade de Refrigerantes comprados: " , quantidadeRefrigerante)
print("Quantidade de Alimentos comprados: " , quantidadeAlimento)
print("----------------------------------------------------------------------------------------")
print("Valor Total de Cervejas compradas: R$ %2.f" % totalCerveja)
print("Valor Total de Refrigerantes comprados: R$ %2.f" % totalRefrigerante)  
print("Valor Total de Alimentos comprados: R$ %2.f" % totalAlimento)
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
print("Valor Total da Compra: R$ %2.f" % valorTotal)
print("----------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------")
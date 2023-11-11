valorTotal = 0
contador = 1
preco = 0

quantidade = int(input("Informe a quantidade de produtos comprados: "))

while contador <= quantidade:
    preco = float(input(f"Informe o valor do {contador}º produto: "))
    
    valorTotal = valorTotal + preco
    
    contador = contador + 1

print("O valor total da compra é de: R$%2.f" % valorTotal)
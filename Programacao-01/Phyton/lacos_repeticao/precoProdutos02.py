valorTotal = 0
continuar = 1
contador = 1
preco = 0

while continuar == 1:
    preco = float(input(f"Informe o valor do {contador}º produto: R$: "))
    
    valorTotal = valorTotal + preco
    
    contador = contador + 1
    
    continuar = int(input("Deseja adicionar mais produtos?\n[ 1 ]=> Sim   ||   [ 2 ]=> Não\n"))

print("O valor total da compra é de: R$%2.f" % valorTotal)
consumo = float(input('Informe o Consumo: '))
estabelecimento = int(input('Qual o tipo de estabelecimento?\n( 1 )-> Residencial  || ( 2 )-> Comercial)\n'))

if(estabelecimento == 1) :
    valor = consumo * 0.03
    print("Valor do produto Nacional: " , valor)

elif(importado == 2) :
    valor = consumo * 0.05
    print("Valor do produto Nacional: " , valor)
    
else :
    print("Opção Invalida!")
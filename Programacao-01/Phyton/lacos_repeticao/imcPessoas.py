contador = 1
magras = 0
normais = 0
gordas = 0

quantidadePessoas = int(input("Informe a quantidade de Pessoas: "))

while contador <= quantidadePessoas:
    peso = float(input(f"Informe o Peso da {contador}º pessoa: "))
    altura = float(input(f"Informe a Altura da {contador}º pessoa: "))
    
    imc = peso / (altura * altura)
    
    if imc < 18.5:
        magras = magras + 1
        
    elif imc <= 25:
        normais = normais + 1
    
    else:
        gordas = gordas + 1
        
    contador = contador + 1
        
print("Número de pessoas Magras: " , magras)
print("Número de pessoas Normais: " , normais)
print("Número de pessoas Gordas: " , gordas)
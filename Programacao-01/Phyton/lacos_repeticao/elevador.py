contador = 1
pesoLimite = 400
pesoTotal = 0

while contador <= 5:
    peso = float(input(f"Informe o Peso da {contador}º pessoa: "))
    pesoTotal = peso + pesoTotal
    contador = contador + 1
    
if pesoTotal <= pesoLimite:
    print(f"Sim, o Elevador suporta as 5 pessoas pois o Limite é 400kg e o peso total das 5 pessoas juntas é de {pesoTotal}kg!")
else:
    print(f"Não, o Elevador não suporta as 5 pessoas pois o Limite é 400kg e o peso total das 5 pessoas juntas é de {pesoTotal}kg!")
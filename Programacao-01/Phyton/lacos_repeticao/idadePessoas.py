contador = 1
grupoUm = 0
grupoDois = 0
grupoTres = 0

while contador <= 7:
    idade = int(input(f"Quantos anos a {contador}º pessoa tem?\n==> "))
    
    if idade < 18:
        grupoUm = grupoUm + 1
        
    elif idade <= 60:
        grupoDois = grupoDois + 1
    
    else:
        grupoTres = grupoTres + 1
        
    contador = contador + 1
        
print("Número de pessoas com menos de 18 anos: " , grupoUm)
print("Número de pessoas entre 18 e 60 anos: " , grupoDois)
print("Número de pessoas com mais de 60 anos: " , grupoTres)
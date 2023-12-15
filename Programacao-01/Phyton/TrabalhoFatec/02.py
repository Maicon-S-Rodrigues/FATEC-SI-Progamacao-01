def CalcularMedia(primeiraNota, segundaNota, terceiraNota):
  media = (primeiraNota + segundaNota + terceiraNota) / 3
  
  if media >= 9 and media <= 10:
    conceito = "A"
    
  elif media >= 8:
    conceito = "B"
    
  elif media >= 7:
    conceito = "C"
    
  elif media >= 6:
    conceito = "D"
    
  else:
    conceito = "F"
    
  return conceito
#------------------------------------------------------------------------>>>
primeiraNota = float(input("Informe a Primeira Nota do Aluno: "))
segundaNota = float(input("Informe a Segunda Nota do Aluno: "))
terceiraNota = float(input("Informe a Terceira Nota do Aluno: "))

resultado = CalcularMedia(primeiraNota, segundaNota, terceiraNota)

if resultado == "A" or resultado == "B":
  print("O Aluno foi Reprovado com nota ", resultado, "!")
  
elif resultado == "C":
  print("O Aluno estará em Recuperação, com nota ", resultado, "!")
  
else:
  print("O Aluno foi Reprovado com nota ", resultado, "!")
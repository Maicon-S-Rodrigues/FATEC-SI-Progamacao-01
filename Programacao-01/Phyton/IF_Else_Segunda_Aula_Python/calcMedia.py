notaUm = float(input("Informe a Primeira Nota: "))
notaDois = float(input("Informe a Segunda Nota: "))

media = (notaUm + notaDois) / 2

if media < 4:
    print("REPROVADO")
elif media < 6:
    print("EXAME")
else:
    print("APROVADO")
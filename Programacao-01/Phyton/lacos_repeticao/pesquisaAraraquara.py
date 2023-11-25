mulheres = 0
homens = 0
salario = 0.0
menorSalario = 0
maiorSalario = 0
mediaIdades = 0
continuar = 1
contador = 1
idade = 0
sexo = 0

while continuar == 1:
    print("----------------------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------------------")
    idade = int(input(f"Informe a idade da {contador}ª pessoa: "))
    sexo = int(input(f"Informe o sexo da {contador}ª pessoa:\n[ 1 ]=> Feminino || [ 2 ]=> Masculino\n"))
    salario = float(input(f"Informe o salário da {contador}ª pessoa: R$ "))
    
    if menorSalario == 0 and maiorSalario == 0:
        menorSalario = salario
        maiorSalario = salario
        
    if sexo == 1:
        mulheres = mulheres + 1
    elif sexo == 2:
        homens = homens + 1
    
    if salario < menorSalario:
        menorSalario = salario
    elif salario > maiorSalario:
        maiorSalario = salario
    
    mediaIdades = mediaIdades + idade
    contador = contador + 1
    
    continuar = int(input("Deseja adicionar mais uma pessoa?\n[ 1 ]=> Sim || [ 2 ]=> Não\n"))

print("----------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------\n")
print("A Quantidade de Mulheres é: ", mulheres)    
print("A Quantidade de Homens é: ", homens, "\n")
print("A Porcentagem de Mulheres é: ", contador * mulheres / 100, "%")
print("A Porcentagem de Homens é: ", contador * homens / 100, "%\n")
print("A Média de idade das pessoas registradas na pesquisa é: ", mediaIdades/contador, "\n")
print("O Maior Salário registrado foi: R$ %2.f"% maiorSalario)
print("O Menor Salário registrado foi: R$ %2.f"% menorSalario)
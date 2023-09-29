altura = float(input('Informe sua altura: '))
sexo = int(input('Informe o seu sexo:\n( 1 )-> Masculino  ||  ( 2 )-> Feminino)\n'))

if(sexo == 1) :
    pesoIdeal = 72.7 * altura - 58
    print("Seu peso ideal é: " , pesoIdeal)

elif(sexo == 2) :
    pesoIdeal = 62.1 * altura - 44.7
    print("Seu peso ideal é: " , pesoIdeal)
    
else :
    print("Opção Invalida!")
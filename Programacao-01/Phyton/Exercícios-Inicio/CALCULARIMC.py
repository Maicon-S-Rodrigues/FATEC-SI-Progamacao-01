peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = (peso / (altura * altura))

print('Índice Massa Corporal (IMC): %.2f' % imc)
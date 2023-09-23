valorDolar = float(input('Informe o preço do Dólar na cotação atual: USD$ '))
valorDesejadoDolar = float(input('Informe quantos Dólares deseja adquirir: USD$ '))

precoEmReais = valorDesejadoDolar * valorDolar

print('Para comprar 20$ USD, você precisa pagar R$' , precoEmReais)
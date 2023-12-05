parar = 1
contadorDePeixes = 1
pesagemTotal = 0
multa = 0
excedente = 0

while parar == 1:
    peso = float(input(f"Informe o peso do {contadorDePeixes}º Peixe: "))
    
    pesagemTotal = pesagemTotal + peso
    
    contadorDePeixes = contadorDePeixes + 1
    
    parar = int(input("Deseja adicionar adicionar mais peixe a conta?\n[1]=> Sim  || [2]=> Não\nEscolha: "))

if pesagemTotal > 10:
    excedente = pesagemTotal - 10
    multa = excedente * 5
    
if multa > 0:
    print("O peso total excedeu o limite gratuito de 10kg!\nO valor de multa pelos %2.f" % excedente,"kg a mais é de R$: %2.f" % multa)
else:
    print("O peso total está dentro do limite gratuito aceito. Não há cobrança de multas! :)")
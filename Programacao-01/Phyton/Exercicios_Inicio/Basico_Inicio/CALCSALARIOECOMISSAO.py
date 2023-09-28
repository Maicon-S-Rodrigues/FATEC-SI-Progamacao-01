salarioFixo = float(input("Informe o Salario do Funcionario: R$ "))
valorDeVendas = float(input("Informe o valor total das vendas realizadas por este Funcionario: R$ "))

comissao = (valorDeVendas * 4) / 100
salarioFinal = salarioFixo + comissao

print("Valor de Comissão: R$ " , comissao)
print("Valor do Salario Final: R$ " , salarioFinal)
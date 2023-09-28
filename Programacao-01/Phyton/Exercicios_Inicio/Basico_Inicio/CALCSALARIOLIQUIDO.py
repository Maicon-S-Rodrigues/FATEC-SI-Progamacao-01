salarioBase = float(input('Informe o Salario Base do Funcionario: R$ '))

aumento = (salarioBase * 10) / 100
salarioBruto = salarioBase + aumento
impostoDeRenda = (salarioBruto * 5) / 100
inss = (salarioBruto * 11) / 100
salarioLiquido = salarioBruto - (impostoDeRenda + inss)

print("Salário Base antes do aumento: R$ " , salarioBase)
print("Aumento: R$ " , aumento)
print("Salário Bruto: R$ " , salarioBruto)
print("----------------------------------")
print("Imposto de Renda: R$ " , impostoDeRenda)
print("INSS: R$ " , inss)
print("----------------------------------")
print("Salário Líquido: R$ " , salarioLiquido)
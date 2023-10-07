salarioBruto = float(input(("Informe o salario do funcionario: ")))

inss = salarioBruto * 11 / 100

if(inss > 820) :
    inss = 820
    
if(salarioBruto < 1500) :
    impostoDeRenda = salarioBruto * 10 / 100
else:
    impostoDeRenda = salarioBruto * 20 / 100

salarioLiquido = salarioBruto - inss - impostoDeRenda
    
print("Salario Bruto informado: ", salarioBruto)
print("INSS: ", inss)
print("Imposto de Renda: ", impostoDeRenda)
print("Salario Líquido: ", salarioLiquido)
Algoritmo "calcSalarioLiquido"

// Descri��o   : Calcular o sal�rio liquido de uma pessoa sabendo-se que
// ela teve aumento de 10%. Sabe-se que � descontado do
// sal�rio o imposto de renda (5%) e o INSS(11%). Calcular
// sal�rio final l�quido

// Autor(a)    : Maicon Siqueira Rodrigues
// Data atual  : 16/09/2023

Var

   salarioLiquido, salarioBase, aumento, impostoDeRenda, inss, salarioBruto: real
   
Inicio

      escreva("Informe o Salario base do Funcionario: R$ ")
      leia(salarioBase)
      
      aumento <- (salarioBase * 10) / 100
      salarioBruto <- salarioBase + aumento
      impostoDeRenda <- (salarioBruto * 5) / 100
      inss <-  (salarioBruto * 11) / 100
      salarioLiquido <- salarioBruto - (impostoDeRenda + inss)
      
      escreval("Sal�rio Base antes do aumento: R$ " , salarioBase)
      escreval("Aumento: R$ " , aumento)
      escreval("Sal�rio Bruto: R$ " , salarioBruto)
      escreval("----------------------------------")
      escreval("Imposto de Renda: R$ " , impostoDeRenda)
      escreval("INSS: R$ " , inss)
      escreval("----------------------------------")
      escreval("Sal�rio L�quido: R$ " , salarioLiquido)
      
Fimalgoritmo
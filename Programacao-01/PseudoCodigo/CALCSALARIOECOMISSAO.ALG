Algoritmo "calcSalarioEComissao"

// Descrição   : Um funcionário recebe um salário fixo mais 4% de comissão
// sobre as vendas. Faça um algoritmo que receba o salário fixo
// de um funcionário e o valor de suas vendas, calcule e mostre a
// comissão e o salário final do funcionário.

// Autor(a)    : Maicon Siqueira Rodrigues
// Data atual  : 16/09/2023

Var

   salarioFixo, salarioFinal, valorDeVendas, comissao: real
   
Inicio

      escreva("Informe o Salario do Funcionario: R$ ")
      leia(salarioFixo)
      
      escreva("Informe o valor total das vendas realizadas por este Funcionario: R$ ")
      leia(valorDeVendas)
      
      comissao <- (valorDeVendas * 4) / 100
      salarioFinal <- salarioFixo + comissao
      
      escreval("Valor de Comissão: R$ " , comissao:)
      escreval("Valor do Salario Final: R$ " , salarioFinal)

Fimalgoritmo
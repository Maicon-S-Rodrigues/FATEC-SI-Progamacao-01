Algoritmo "calcSalarioEComissao"

// Descri��o   : Um funcion�rio recebe um sal�rio fixo mais 4% de comiss�o
// sobre as vendas. Fa�a um algoritmo que receba o sal�rio fixo
// de um funcion�rio e o valor de suas vendas, calcule e mostre a
// comiss�o e o sal�rio final do funcion�rio.

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
      
      escreval("Valor de Comiss�o: R$ " , comissao:)
      escreval("Valor do Salario Final: R$ " , salarioFinal)

Fimalgoritmo
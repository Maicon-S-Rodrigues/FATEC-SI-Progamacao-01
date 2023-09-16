Algoritmo "calcContaEnergia"

// Descrição   : Calcular o valor da conta de Energia de uma residência
//sabendo-se que o valor do Kw é de R$0,30.
//Mas como estamos em um período de seca então utiliza-se
//BANDEIRA VERMELHA, o que proporciona um acréscimo de
//10% no valor da conta.
//Faça um pseudocódigo/algoritmo que calcule o valor da conta.

// Autor(a)    : Maicon Siqueira Rodrigues
// Data atual  : 16/09/2023
Var

   valorKw, kwConsumidos, valorConta: real

Inicio

      valorKw <- 0.30
      
      escreva("O preço do Kw consumido é de R$0,30")
      escreval("Informe quantos Kw foram consumidos: ")
      leia(kwConsumidos)

      valorConta <- valorKw * kwConsumidos
      valorConta <- valorConta + ((valorConta * 10) / 100)
      
      escreva("O preço para conta de Energia será de: R$" , valorConta)


Fimalgoritmo
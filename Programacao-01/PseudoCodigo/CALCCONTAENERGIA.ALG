Algoritmo "calcContaEnergia"

// Descri��o   : Calcular o valor da conta de Energia de uma resid�ncia
//sabendo-se que o valor do Kw � de R$0,30.
//Mas como estamos em um per�odo de seca ent�o utiliza-se
//BANDEIRA VERMELHA, o que proporciona um acr�scimo de
//10% no valor da conta.
//Fa�a um pseudoc�digo/algoritmo que calcule o valor da conta.

// Autor(a)    : Maicon Siqueira Rodrigues
// Data atual  : 16/09/2023
Var

   valorKw, kwConsumidos, valorConta: real

Inicio

      valorKw <- 0.30
      
      escreva("O pre�o do Kw consumido � de R$0,30")
      escreval("Informe quantos Kw foram consumidos: ")
      leia(kwConsumidos)

      valorConta <- valorKw * kwConsumidos
      valorConta <- valorConta + ((valorConta * 10) / 100)
      
      escreva("O pre�o para conta de Energia ser� de: R$" , valorConta)


Fimalgoritmo
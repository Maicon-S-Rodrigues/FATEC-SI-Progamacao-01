Algoritmo "imobiliaria"

// Descri��o   : A imobili�ria Im�bilis vende apenas terrenos retangulares.
// Fa�a um algoritmo para ler as dimens�es de um terreno. Depois
// calcular a �rea do terreno e o valor do terreno, sabendo que o
//  valor do m2 � de R$500,00.

// Autor(a)    : Maicon Siqueira Rodrigues
// Data atual  : 16/09/2023

Var

   base, altura, area, valor: real
   
Inicio

      escreva("Qual a Base do terreno? ")
      leia(base)
      
      escreva("Qual a Altura do terreno? ")
      leia(altura)
      
      area <- base * altura
      valor <- area * 500
      
      escreval("A Area do terreno � de: " , area)
      escreval("O valor do terreno �: R$" , valor)

Fimalgoritmo
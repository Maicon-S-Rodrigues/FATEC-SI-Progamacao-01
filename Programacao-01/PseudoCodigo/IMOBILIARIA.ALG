Algoritmo "imobiliaria"

// Descrição   : A imobiliária Imóbilis vende apenas terrenos retangulares.
// Faça um algoritmo para ler as dimensões de um terreno. Depois
// calcular a área do terreno e o valor do terreno, sabendo que o
//  valor do m2 é de R$500,00.

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
      
      escreval("A Area do terreno é de: " , area)
      escreval("O valor do terreno é: R$" , valor)

Fimalgoritmo
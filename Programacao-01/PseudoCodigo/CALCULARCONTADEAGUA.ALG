Algoritmo "CalcularContaDeAgua"
// Disciplina  : Programa��o 01
// Professor   : Ca��o
// Descri��o   : Calcula conta de Agua
// Autor(a)    : Maicon Siqueira Rodrigues
// Data atual  : 26/08/2023
Var
   litrosDeAgua, valorDaConta: real

Inicio
      escreva ("Informe quantos Litros de �gua foram consumidos: ")
      leia (litrosDeAgua)

      valorDaConta <- litrosDeAgua * 0.05

      escreva ("O valor da conta de �gua � R$: ")
      escreva (valorDaConta:2:3)
Fimalgoritmo
Algoritmo "CalcularContaDeAgua"
// Disciplina  : Programação 01
// Professor   : Cação
// Descrição   : Calcula conta de Agua
// Autor(a)    : Maicon Siqueira Rodrigues
// Data atual  : 26/08/2023
Var
   litrosDeAgua, valorDaConta: real

Inicio
      escreva ("Informe quantos Litros de água foram consumidos: ")
      leia (litrosDeAgua)

      valorDaConta <- litrosDeAgua * 0.05

      escreva ("O valor da conta de água é R$: ")
      escreva (valorDaConta:2:3)
Fimalgoritmo
Algoritmo "CalcularIMC"
// Disciplina  : Programação 01
// Professor   : Cação
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Maicon Siqueira Rodrigues
// Data atual  : 26/08/2023
Var
   peso, altura, imc: real

Inicio
      escreva ("Informe seu peso (Ex: 85, 88.2, etc): ")
      leia (peso)
      
      escreva ("Informe sua altura (Ex: 1.75, 1.68, etc): ")
      leia (altura)
      
      imc <- (peso / (altura * altura))
      
      escreva ("Indice Massa Corporal (IMC): ")
      escreva (imc:2:2)
Fimalgoritmo
Algoritmo "VelocidadeMedia"
// Disciplina  : Programa��o 01
// Professor   : Ca��o
// Descri��o   : Calcula a velocidade media de uma cidade para outra
// Autor(a)    : Maicon Siqueira Rodrigues
// Data atual  : 26/08/2023
Var
   distancia, tempoGasto, velocidadeMedia: real

Inicio
      escreva ("Informe a distancia percorrida: ")
      leia (distancia)
      
      escreva ("Informe o tempo que a viagem durou: ")
      leia (tempoGasto)

      velocidadeMedia <- distancia / tempoGasto

      escreva ("A Velocidade M�dia foi: " , velocidadeMedia:2:3)
Fimalgoritmo
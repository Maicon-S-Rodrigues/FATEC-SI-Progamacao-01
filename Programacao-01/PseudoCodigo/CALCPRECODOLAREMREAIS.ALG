Algoritmo "calcPrecoDolarEmReais"

// Descri��o   : Uma pessoa vai viajar para o exterior e precisa comprar
// d�lares. Fazer um algoritmo que leia o valor do d�lar
// (cota��o do dia) e quantos d�lares a pessoa deseja
//comprar. Calcular quantos reais s�o necess�rios para
//comprar os dolares

// Autor(a)    : Maicon Siqueira Rodrigues
// Data atual  : 16/09/2023

Var

   valorDolar, valorDesejadoDolar, precoEmReais: real

Inicio

      escreva("Informe o pre�o do D�lar na cota��o atual: USD$")
      leia(valorDolar)
      
      escreva("Informe quantos D�lares deseja adquirir: USD$")
      leia(valorDesejadoDolar)
      
      precoEmReais <- valorDesejadoDolar * valorDolar
      
      escreva("Para comprar 20$ USD, voc� precisa pagar R$" , precoEmReais)

Fimalgoritmo
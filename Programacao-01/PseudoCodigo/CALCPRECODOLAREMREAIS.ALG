Algoritmo "calcPrecoDolarEmReais"

// Descrição   : Uma pessoa vai viajar para o exterior e precisa comprar
// dólares. Fazer um algoritmo que leia o valor do dólar
// (cotação do dia) e quantos dólares a pessoa deseja
//comprar. Calcular quantos reais são necessários para
//comprar os dolares

// Autor(a)    : Maicon Siqueira Rodrigues
// Data atual  : 16/09/2023

Var

   valorDolar, valorDesejadoDolar, precoEmReais: real

Inicio

      escreva("Informe o preço do Dólar na cotação atual: USD$")
      leia(valorDolar)
      
      escreva("Informe quantos Dólares deseja adquirir: USD$")
      leia(valorDesejadoDolar)
      
      precoEmReais <- valorDesejadoDolar * valorDolar
      
      escreva("Para comprar 20$ USD, você precisa pagar R$" , precoEmReais)

Fimalgoritmo
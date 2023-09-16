Algoritmo "calcGasolina"

// Descrição   : Um motorista deseja colocar no seu tanque X reais de
// gasolina. Escreva um algoritmo para ler o preço do litro
// da gasolina e o valor do pagamento(X), e exibir quantos
// litros ele conseguiu colocar no tanque.

// Autor(a)    : Maicon Siqueira Rodrigues
// Data atual  : 16/09/2023

Var

   precoGasolina, valorPago, litrosGasolina: real

Inicio

      escreva("Informe qual o valor do litro de gasolina: R$")
      leia(precoGasolina)
      
      escreva("Informe qual o valor que deseja colocar: R$")
      leia(valorPago)
      
      litrosGasolina <- valorPago / precoGasolina
      
      escreva("Com o valor informado, sera possível adicionar " , litrosGasolina)
      escreva(" litros de Gasolina.")
      

Fimalgoritmo
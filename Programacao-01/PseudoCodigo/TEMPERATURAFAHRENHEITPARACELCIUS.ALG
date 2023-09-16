Algoritmo "temperaturaFahrenheitParaCelcius"

// Descrição   : Alguns países medem temperaturas em graus Celsius, e
// outros em graus Fahrenheit. Faça um algoritmo para ler uma
// temperatura Fahrenheit e transforma-la em Celsius

// Autor(a)    : Maicon Siqueira Rodrigues
// Data atual  : 16/09/2023

Var

   fahrenheit, celcius: real
   
Inicio

      escreva("Informe a Temperatura Fahrenheit que deseja converter: °F ")
      leia(fahrenheit)
      
      celcius <- (5 / 9) * (fahrenheit - 32)
      
      escreva("A temperatura em Celsius é: " , celcius:2:2, " °C")

Fimalgoritmo
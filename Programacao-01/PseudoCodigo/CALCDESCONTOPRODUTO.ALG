Algoritmo "calcDescontoProduto"
// Descri��o   : Calcular o pre�o final de um produto que tem desconto de 30%
// sobre o pre�o atual
// Autor(a)    : Maicon Siqueira Rodrigues
// Data atual  : 16/09/2023
Var
   precoAtual, precoFinal: Real
Inicio
      escreva("Informe o pre�o atual do produto: ")
      leia(precoAtual)
      
      precoFinal <- precoAtual - ((precoAtual * 30) / 100)
      
      escreva("O pre�o final do produto com o desconto aplicado �: " , precoFinal)
Fimalgoritmo
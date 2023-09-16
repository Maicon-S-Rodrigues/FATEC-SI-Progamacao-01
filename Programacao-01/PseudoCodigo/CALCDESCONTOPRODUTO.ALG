Algoritmo "calcDescontoProduto"
// Descrição   : Calcular o preço final de um produto que tem desconto de 30%
// sobre o preço atual
// Autor(a)    : Maicon Siqueira Rodrigues
// Data atual  : 16/09/2023
Var
   precoAtual, precoFinal: Real
Inicio
      escreva("Informe o preço atual do produto: ")
      leia(precoAtual)
      
      precoFinal <- precoAtual - ((precoAtual * 30) / 100)
      
      escreva("O preço final do produto com o desconto aplicado é: " , precoFinal)
Fimalgoritmo
ano = 0
toneladas = 5

while toneladas <= 10:
    toneladas = toneladas + 0.10 * toneladas
    ano = ano + 1
    
print(f"Alcançará 10 toneladas em {ano} anos.")
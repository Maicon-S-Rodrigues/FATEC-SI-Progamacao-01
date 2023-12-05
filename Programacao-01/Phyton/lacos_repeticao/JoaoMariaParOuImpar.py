#Maria == ÍMPAR
#João == PAR

rodada = 1
vitoriasMaria = 0
vitoriasJoao = 0

while rodada <= 5:
    joao = 0
    maria = 0
    
    print(f"{rodada}º Rodada!")
    joao = int(input("Escolha do João: "))
    maria = int(input("Escolha da Maria: "))
    
    resultado = joao + maria
    
    if resultado % 2 == 0:
        vitoriasJoao = vitoriasJoao + 1
        print(f"Vencedor da {rodada}º Rodada: João!")
    else:
        vitoriasMaria = vitoriasMaria + 1
        print(f"Vencedor da {rodada}º Rodada: Maria!")
    
    print("----------------------------------------------------")
    
    if vitoriasJoao == 3:
        print("João venceu a melhor de 5 com 3 vitórias!")
        print(f"Maria teve {vitoriasMaria} vitórias...")
        break
    
    elif vitoriasMaria == 3:
        print("Maria venceu a melhor de 5 com 3 vitórias!")
        print(f"João teve {vitoriasJoao} vitórias...")
        break
    
    rodada = rodada + 1
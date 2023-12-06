def calcularFX(count):
    x = 2 * count**2 - 3 * count + 5
    x = round(x, 3)
    
    print(f"F({count}) = 2 * X^² - 3 * X + 5 = {x}")
        
        
        
x = 0
count = 0     
 
while count <= 10:
    calcularFX(count)
    count = count + 1
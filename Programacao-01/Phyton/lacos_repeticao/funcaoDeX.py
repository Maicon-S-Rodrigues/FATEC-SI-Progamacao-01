x = 0
count = 0

while count <= 10:
    x = 2 * count**2 - 3 * count + 5
    x = round(x, 3)
    
    print(f"F({count}) = 2 * X^² - 3 * X + 5 = {x}")
    
    count = count + 1
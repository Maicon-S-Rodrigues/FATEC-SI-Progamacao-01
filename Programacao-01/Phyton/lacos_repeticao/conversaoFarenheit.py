celsius = 0
farenheit = 0

while farenheit <= 100:
    celsius = (5 / 9) * (farenheit - 32)
    
    print("Para Farenheit = ", farenheit, ", o valor em Celsius é: %2.f" % celsius)
    
    farenheit = farenheit + 1
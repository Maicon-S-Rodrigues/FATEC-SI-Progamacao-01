def converterTemperatura(farenheit):
    return (5.0/9.0)*(farenheit-32)

temperatura = float(input("Informe a temperatura em Farenheit que deseja converter: "))

print("A temperatura %2.f" % temperatura, "º Farenheit, convertida para Celsius é: %2.f" % converterTemperatura(temperatura))
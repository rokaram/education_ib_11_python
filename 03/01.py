def temperature_assessment(temp):
    return "Жарко" if temp > 28 else "Холодно" if temp < 15.5 else "Нормально"


temperature = float(input("Enter the temperature: "))
print(temperature_assessment(temperature))

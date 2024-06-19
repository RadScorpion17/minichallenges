def celsius_a_fahrenheit(temperatura : float) -> float:
    return (temperatura * 9/5) + 32


user_input = float(input("Ingrese una temperatura: "))
print(celsius_a_fahrenheit(user_input))

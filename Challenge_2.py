# Tabla de multiplicar e numero dado

def tabla_multiplicar(numero: int):
    return [numero * i for i in range(1, 11)]


user_input: int = int(input("Numero a multiplicar: "))
print(tabla_multiplicar(user_input))

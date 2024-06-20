import random


# 0 : Seguir jugando ; 1 - Gana usuario ; 2 - Gana PC
def validar_estado(user: str, pc: str) -> int:
    if user == pc:
        return 0
    if (user == 'piedra' and pc == 'tijera') or (user == 'papel' and pc == 'piedra') or (
            user == 'tijera' and pc == 'papel'):
        return 1

    return 2


opciones = {1: 'piedra', 2: 'papel', 3: 'tijera'}

jugando = True
while jugando:
    user_input = int(input("Selecciona un movimiento: \n1- Piedra \n2- Papel \n3- Tijera \n"))

    if user_input not in opciones:
        print("Entrada no válida. Intenta de nuevo.")
        continue

    movimiento_usuario = opciones[user_input]
    value = random.randint(1, 3)
    movimiento_computadora = opciones[value]

    print(f"Tú: {movimiento_usuario} | Computadora: {movimiento_computadora}")

    estado = validar_estado(movimiento_usuario, movimiento_computadora)

    if estado == 1:
        print("¡Ganaste")
        jugando = False
    elif estado == 2:
        print("Perdiste")
        jugando = False
    else:
        print("Empate")

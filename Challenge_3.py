# Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.

def contar_vocales(texto: str) -> int:
    vocales: tuple = ('a', 'e', 'i', 'o', 'u')
    cont = 0
    for letra in texto.lower():
        cont += 1 if letra in vocales else 0

    return cont


user_input = input("Ingrese un texto: ")
print(contar_vocales(user_input))

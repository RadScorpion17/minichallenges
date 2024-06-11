def invertir_string(texto: str) -> str:
    new_text = ''
    for char in reversed(texto):
        new_text += char

    return new_text


user_input = input("Inserte una palabra: ")
reversed_user_input = invertir_string(user_input)
print(reversed_user_input)

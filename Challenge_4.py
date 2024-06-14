def ordenar_lista(lista : list) -> list:
    return sorted(lista)


lista_usuario = []

for i in range(5):
    lista_usuario.append(int(input(f'Numero {i+1}: ')))

print(lista_usuario)
print(ordenar_lista(lista_usuario))

# Devuelve la cantidad de veces que se repite un curso (agregarla previamente a la lista) dentro de la lista
# luego elimina el primer ítem de la lista usando debidamente su índice.

lista_cursos = [
    "Matemáticas",
    "Fisica",
    "Programación",
    "Bases de Datos",
    "Inteligencia Artificial",
    "Redes",
]

lista_cursos.append("Programación")

print(lista_cursos)

cursos_repetidos = lista_cursos.count("Programación")
print(cursos_repetidos)


# elminar el primer elemento de la lista usando su indice

del lista_cursos[0]

print("Lista Final: \n")
print((lista_cursos))

# 2 Agregar 4 Objetos nuevos a tu lista (append) y quitar 2 elementos de tu nueva lista ítems por valor, no por índice.
# Mostrar la lista final por consola

lista_cursos = [
    "Matemáticas",
    "Fisica",
    "Programación",
    "Bases de Datos",
    "Inteligencia Artificial",
    "Redes",
]
print("Lista de curso Original")
print(lista_cursos)
print("")


lista_cursos.append("Quimica")
lista_cursos.append("Biologia")
lista_cursos.append("Ciencias")
lista_cursos.append("Geografia")

print("Lista de curso despues de agregar 4 cursos")
print(lista_cursos)
print("")

lista_cursos.remove("Fisica")
lista_cursos.remove("Ciencias")

print("")
print("listas de curso despues de eliminar 2 cursos")
print(lista_cursos)


print(f"la cantida total de cursos de la lista es:{len(lista_cursos)} ")

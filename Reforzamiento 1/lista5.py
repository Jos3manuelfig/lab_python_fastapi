# Sumar las dos listas creadas anteriormente y mostrar el resultado en terminal.
from sqlalchemy import literal

lista_cursos = [
    "Matemáticas",
    "Fisica",
    "Programación",
    "Bases de Datos",
    "Inteligencia Artificial",
    "Redes",
]

mi_lista = []

mi_lista.append(3.14)
mi_lista.append(345)
mi_lista.append([2, 4, 5, 6])
mi_lista.append("mi_lista2")


listaResul = lista_cursos + mi_lista

print(listaResul)

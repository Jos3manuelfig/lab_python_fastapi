from sys import set_coroutine_origin_tracking_depth


# 1. Crear una lista de 6 objetos y mostrar en pantalla (ítems de cursos que lleves o hayas llevado en la universidad) e
# Invierte y muestra en consola tu lista de cursos.

lista_cursos = [
    "Matemáticas",
    "Física",
    "Programación",
    "Bases de Datos",
    "Inteligencia Artificial",
    "Redes",
]

lista_cursos_inverida = sorted(lista_cursos)
print("Lista de cursos Original")
print(lista_cursos)
print("\n")
print(lista_cursos_inverida)

# Crear una lista (entre floats y bools, 6 elementos mínimo) donde imprimas el penúltimo y último valor (por índice)
#

mi_lista = ["3.14", 23, -1, True, [1, 2, 3], 1.23]

print(mi_lista[-1])
print(mi_lista[-2])


for index, elemento in enumerate(mi_lista):
    print(f"Elemto : {index} es de Tipo: {type(elemento)} ")

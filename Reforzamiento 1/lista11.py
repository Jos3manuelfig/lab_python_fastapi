# Crear una lista con los primeros 15 números impares
my_lista = [x for x in range(1, 30) if x % 2 == 1]


my_lista.append(1.7)
my_lista.append(3.14)
my_lista.append(1.7)


my_lista.insert(3, "cadena")


print("Lista antes de eliminar la cadena:")
print(my_lista)


del my_lista[3]


print("\nLista después de eliminar la cadena:")
print(my_lista)

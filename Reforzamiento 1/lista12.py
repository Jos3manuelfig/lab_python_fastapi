# Crea una lista vacía (con 10 posiciones), pide sus valores y devuelve la suma y la media de los números.


lista = [0] * 3

#
for i in range(len(lista)):
    while True:
        try:
            valor = int(input(f"Ingrese un número para la posición {i + 1}: "))
            lista[i] = valor
            break
        except ValueError:
            print("Ingrese un número válido.")


suma = sum(lista)
media = suma / len(lista)

# Mostrar resultados
print(f"\nLista completada: {lista}")
print(f"La suma de los números ingresados es: {suma}")
print(f"El promedio de los números ingresados es: {media}")


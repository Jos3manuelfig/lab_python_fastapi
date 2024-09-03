"""
Programación funcional en Python

Ejercicio en clase
"""

"""
Requisitos:
- Solicitar al usuario 4 números por consola
- Crear una función que devuelva cuál es el mayor número de los 4 ingresado por el usuario
- Finalmente elevar al cubo este resultado
"""

def solicitar_numeros():
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    numero3 = int(input("Ingrese el tercer número: "))
    numero4 = int(input("Ingrese el cuarto número: "))
    return numero1, numero2, numero3, numero4

def obtener_mayor_numero(numero1, numero2, numero3, numero4):
    # Encontrar el mayor número entre los cuatro
    return max(numero1, numero2, numero3, numero4)

def elevar_al_cubo(numero):
    # Elevar el número al cubo
    return numero ** 3

def main():
    # Paso 1: Solicitar números
    numero1, numero2, numero3, numero4 = solicitar_numeros()

    # Paso 2: Obtener el mayor número
    mayor_numero = obtener_mayor_numero(numero1, numero2, numero3, numero4)
    print(f"El mayor número es: {mayor_numero}")

    # Paso 3: Elevar al cubo el mayor número
    resultado = elevar_al_cubo(mayor_numero)
    print(f"El mayor número elevado al cubo es: {resultado}")

if __name__ == "__main__":
    main()

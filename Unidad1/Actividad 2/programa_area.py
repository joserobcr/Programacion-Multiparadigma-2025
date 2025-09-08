import math

print("Cálculo de áreas")
print("1. Triángulo")
print("2. Cuadrado")
print("3. Círculo")

opcion = int(input("Elige una figura (1-3): "))

if opcion == 1:
    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area}")

elif opcion == 2:
    lado = float(input("Ingresa el lado del cuadrado: "))
    area = lado ** 2
    print(f"El área del cuadrado es: {area}")

elif opcion == 3:
    radio = float(input("Ingresa el radio del círculo: "))
    area = math.pi * (radio ** 2)
    print(f"El área del círculo es: {area}")

else:
    print("Opción no válida.")
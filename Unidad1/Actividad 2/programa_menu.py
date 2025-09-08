while True:
    print("\n--- Menú ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print(f"La suma es: {a + b}")

    elif opcion == "2":
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print(f"La resta es: {a - b}")

    elif opcion == "3":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción inválida. Intenta de nuevo.")
from functools import reduce

def crear_transformador(funcion):
    """
    Recibe una función de transformación (ej. x * 2) y retorna 
    una NUEVA función que sabe aplicar eso a toda una lista.
    """
    def transformador(lista):
        # Aplicamos map y convertimos a lista
        return list(map(funcion, lista))
    return transformador

def crear_filtro(predicado):
    """
    Recibe una condición (predicado) y retorna una NUEVA función
    que sabe filtrar una lista con esa condición.
    """
    def filtro(lista):
        # Aplicamos filter y convertimos a lista
        return list(filter(predicado, lista))
    return filtro

def crear_reductor(funcion, valor_inicial):
    """
    Recibe una función de acumulación y un valor inicial.
    Retorna una nueva función que reduce una lista a un solo valor.
    """
    def reductor(lista):
        return reduce(funcion, lista, valor_inicial)
    return reductor

def componer(*funciones):
    """
    Recibe múltiples funciones como argumentos.
    Retorna una función 'pipeline' que pasa el resultado de una 
    función como entrada de la siguiente (de izquierda a derecha).
    """
    def pipeline(data):
        resultado = data
        for f in funciones:
            resultado = f(resultado)
        return resultado
    return pipeline

# --- Pruebas y Ejecución ---

if __name__ == "__main__":
    # Datos de prueba
    numeros = [1, -2, 3, -4, 5, -6, 7, 8, -9, 10]

    print(f"Entrada original: {numeros}")

    # Pipeline
    pipeline = componer(
        crear_filtro(lambda x: x > 0),         
        crear_transformador(lambda x: x ** 2),  
        crear_reductor(lambda acc, x: acc + x, 0) 
    )

    resultado = pipeline(numeros)
    
    print(f"Resultado final: {resultado}") 
    
    esperado = 248
    if resultado == esperado:
        print("El cálculo es correcto.")
    else:
        print(f"Error. Se esperaba {esperado} pero se obtuvo {resultado}.")
# Parte 1: Identificación y Análisis

## Función A: `calcular_promedio`
* **Tipo:** Pura.
* **Análisis:**
    1. El resultado depende únicamente de los argumentos de entrada.
    2. No modifica la lista original ni variables externas.
* **Conversión:** No aplica.

## Función B: `siguiente_id`
* **Tipo:** Impura.
* **Análisis:**
    1. **Estado Global:** Utiliza la palabra clave "global" para depender de una variable externa.
    2. **Efecto Secundario:** Modifica la variable externa cada vez que se ejecuta.
* **Conversión a Pura:**
    Se debe eliminar la dependencia global pasando el contador como argumento y devolviendo el nuevo valor.
    ```python
    def siguiente_id_puro(contador_actual):
        nuevo_contador = contador_actual + 1
        return nuevo_contador, f"ID-{nuevo_contador}"
    ```

## Función C: `agregar_fecha`
* **Tipo:** Impura.
* **Análisis:**
    1. **Mutabilidad:** Modifica directamente el diccionario "registro" que recibe (efecto secundario).
    2. **No determinismo:** Usa "datetime.now()", por lo que el resultado cambia según el momento de ejecución, rompiendo la transparencia referencial.
* **Conversión a Pura:**
    Se debe crear una copia del diccionario y recibir la fecha como parámetro para que sea predecible.
    ```python
    def agregar_fecha_pura(registro, fecha_fija):
        nuevo_registro = registro.copy() 
        nuevo_registro['fecha'] = fecha_fija
        return nuevo_registro
    ```

## Función D: `filtrar_positivos`
* **Tipo:** Pura.
* **Análisis:**
    1. Utiliza una *list comprehension* que genera una **nueva lista**, dejando la original intacta.
    2. Su salida depende solo de la entrada.
* **Conversión:** No aplica (ya es correcta).

## Función E: `mezclar_lista`
* **Tipo:** Impura.
* **Análisis:**
    1. **Mutabilidad:** La función "random.shuffle(lista)" desordena la lista original *in-place* (sobre la misma memoria).
    2. **Aleatoriedad:** El resultado no es predecible sin una semilla controlada.
* **Conversión a Pura:**
    Utilizar "random.sample" para generar una nueva lista desordenada sin tocar la original.
    ```python
    import random
    def mezclar_lista_pura(lista):
        return random.sample(lista, len(lista))
    ```


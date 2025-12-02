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

# Parte 4: Reflexión Metacognitiva

## 1. ¿Qué significa que una función sea "pura"?
Que una función sea pura significa que su comportamiento es totalmente predecible y aislado del resto del sistema. Esto implica que, para una misma entrada, siempre devolverá exactamente el mismo resultado, sin importar cuántas veces se ejecute. No modifica variables externas, no escribe en archivos, ni altera el estado de la aplicación fuera de su propio ámbito. 
Ejemplo: Una calculadora simple es pura, porque si escribes "2+2" siempre dará "4", sin importar si es de día, si hace frío o si la usaste mil veces antes.

## 2. En la Parte 3, ¿por qué `crear_transformador` retorna una función en lugar de aplicar directamente la transformación? ¿Qué ventaja ofrece este diseño?
Esta función devuelve otra función para separar la lógica de la operación de los datos reales. Esto permite configurar "qué hacer" antes de tener la lista de datos lista. La ventaja principal es que podemos reutilizar esa lógica específica muchas veces en diferentes partes del código. Facilita conectar varias funciones pequeñas para crear procesos complejos de forma ordenada.

## 3. ¿Qué dificultades encontraste al convertir el código imperativo a funcional en la Parte 2? ¿Qué parte fue más difícil y cómo la resolviste?
Sinceramente, lo que más me costó fue quitarme la costumbre de querer usar un ciclo for para todo. Estaba muy tentado a declarar una variable total e ir sumándole valores de uno en uno, porque así es como aprendí a programar desde el inicio.

## 4. Si tuvieras que explicar la diferencia entre programación imperativa y funcional a alguien que no programa, ¿qué analogía usarías?
Usaría la analogía de preparar una cena. 
La Programación Imperativa es como un cocinero solitario y algo desorganizado que hace todo él mismo: corta la cebolla, luego corre a la estufa, luego lava el plato, luego vuelve a cortar; si se equivoca en un paso, puede arruinar todo el plato porque todo depende de su memoria y estado actual.
La Programación Funcional, en cambio, es como una línea de ensamblaje industrial especializada. Hay una estación que solo lava verduras, otra que solo corta y otra que solo cocina; los ingredientes pasan por una banda transportadora de una estación a otra. Cada estación es experta en su tarea, no necesita saber qué pasa en el resto de la fábrica, y el resultado final es siempre consistente y libre de errores humanos por cansancio.
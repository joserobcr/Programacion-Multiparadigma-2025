# Sistema de Gestión de Inventario

Esta actividad implementa un sistema basico de inventario utilizando Programacion Orientada a Objetos en Python, centrandose en los principios de Encapsulacion y Abstraccion mediante el uso de atributos con modificadores de acceso, propiedades, y metodos especiales.

# Estructura del Proyecto

El codigo esta organizado en tres archivos principales para una mejor modularidad y separacion de responsabilidades:

- **producto.py**: Define la clase "Producto".
- **inventario.py**: Define la clase "Inventario", que gestiona la coleccion de productos.
- **main.py**: Contiene la logica principal para instanciar, manipular y demostrar el sistema.

# Explicacion del Diseño

El diseño de este sistema se basa en la aplicacion estricta de dos pilares de la POO: Encapsulacion y Abstraccion.

## Encapsulacion

La encapsulacion se aplica para proteger los datos internos de las clases y garantizar su integridad, forzando la interaccion a traves de interfaces controladas.

- Atributo "__stock" en la clase "Producto": El stock es critico; su modificacion requiere una validacion estricta para asegurar que nunca sea menor a 0. 
- Atributo "_precio" en la clase "Producto": El precio es fundamental, se valida para que sea mayor a 0, pero se marca como protegido para indicar que no debe ser modificado directamente fuera de la clase o subclases. 
- Atributo "__productos" en la clase "Inventario": La estructura interna del inventario esta completamente oculta. La unica forma de interactuar con la lista es a traves de metodos publicos como "agregar_producto" o "buscar_producto". 

## Uso de Getters y Setters (@property)

En lugar de exponer los atributos directamente, utilizamos "@property" para definir propiedades controladas:

- Getter (@property): Permite obtener el valor del atributo privado (__stock, _precio) de forma segura, como si fuera un atributo publico.
- Setter (@stock.setter / @precio.setter): Permite modificar el valor, pero solo despues de aplicar una logica de validacion.
    * Ejemplo: El setter de "stock" en la clase "Producto" lanza un "ValueError" si se intenta asignar un valor negativo, asegurando la coherencia de los datos del inventario.

## Abstraccion

La abstraccion se logra principalmente en la clase "Inventario":

- El usuario de la clase "Inventario" no necesita saber como se almacenan los productos. Solo utiliza los metodos publicos como "agregar_producto" o "buscar_producto".
- El metodo "total_valor_inventario()" oculta la complejidad del calculo y simplemente retorna el valor agregado.

## Metodos Especiales Implementados

Se han utilizado metodos especiales para mejorar la interoperabilidad y legibilidad de las clases:

Metodo Especial "__init__": Constructor, inicializa y valida los atributos con los setters. 
Metodo Especial "__str__": Permite imprimir el objeto "Producto" de forma legible. 
Metodo Especial "__eq__": Define la comparacion de igualdad basada unicamente en el nombre del producto. 
Metodo Especial "__init__": Constructor, inicializa el diccionario privado de productos. 
Metodo Especial "__len__": Permite usar la funcion nativa "len()" para obtener el numero de productos unicos. 
Metodo Especial "__str__": Permite imprimir el objeto "Inventario", listando todos los productos que contiene. 
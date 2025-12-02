def es_venta_valida(venta):
    """
    Función Pura (Filtro):
    Decide si una venta debe ser procesada.
    Condición: Monto mayor a 100.
    """
    return venta['monto'] > 100

def aplicar_formato_impuesto(venta):
    """
    Función Pura (Transformación/Map):
    Recibe una venta y crea un NUEVO diccionario con el impuesto aplicado.
    No modifica el diccionario original (Inmutabilidad).
    """
    monto_con_impuesto = venta['monto'] * 1.15
    return {
        'id': venta['id'],
        'monto_original': venta['monto'],
        'monto_final': monto_con_impuesto
    }


def procesar_ventas_funcional(ventas):
    """
    Orquesta el proceso usando funciones como ciudadanos de primera clase.
    En lugar de un bucle, usamos un flujo de datos:
    Entrada -> Filtrar -> Transformar -> Resultado
    """
    
    # PASO 1: Filtrar 
    ventas_filtradas = filter(es_venta_valida, ventas)
    
    # PASO 2: Mapear 
    ventas_procesadas = list(map(aplicar_formato_impuesto, ventas_filtradas))
    
    # PASO 3: Reducir/Agregar 
    total_acumulado = sum(v['monto_final'] for v in ventas_procesadas)
    
    return ventas_procesadas, total_acumulado


ventas_ejemplo = [ 
    {'id': 1, 'monto': 50},
    {'id': 2, 'monto': 150},
    {'id': 3, 'monto': 200},
    {'id': 4, 'monto': 80},
    {'id': 5, 'monto': 300},
]

lista_final, gran_total = procesar_ventas_funcional(ventas_ejemplo)

print("--- Resultado del Procesamiento Funcional ---")
print(f"Lista Procesada: {lista_final}")
print(f"Total Acumulado: {gran_total}")
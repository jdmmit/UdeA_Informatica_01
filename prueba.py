def analizar_tupla(numeros):
    maximo = max(numeros)
    minimo = min(numeros)
    promedio = sum(numeros) / len(numeros)
    print(f"El valor máximo es {maximo}")
    print(f"El valor mínimo es {minimo}")
    print("El valor promedio es", promedio)
# Ejemplo de uso:
tupla = (1, 2, 4, 6, 3, 2, 7, 4, 3, 4)
analizar_tupla(tupla)


diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
def imprimir_diccionario(dic):
    for clave, valor in dic.items():
        print(f"{clave}: {valor}")
# Ejemplo de uso:
imprimir_diccionario(diccionario)
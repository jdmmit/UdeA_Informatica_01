# Ejercicio 3.2
"""
3.2. Realice un programa que permita cambiar los espacios “ ” en una oración por un guión “-” Nota: No se permite el uso de la instrucción replace(), solo instrucciones básicas.

"""


# a) Análisis del problema
"""
Concepto	Descripción
Entrada	    Una cadena (oración) escrita por el usuario, p. ej. "hola mundo cruel"
Proceso	    Recorrer la cadena carácter por carácter.Si el carácter es un espacio (" "), añadir "-" al resultado.Si no, añadir el mismo carácter.
Salida	    La misma oración pero con los espacios reemplazados por guiones, p. ej. "hola-mundo-cruel"

"""
# b) Algoritmo en diagrama de flujo

"""

┌───────────┐
│  INICIO   │
└────┬──────┘
     │
     ▼
┌───────────────┐
│ Leer ORACION  │
└────┬──────────┘
     │
     ▼
┌───────────────────┐
│ resultado ← ""    │
└────┬──────────────┘
     │
     ▼
┌─────────────┐
│ i = 0       │
└────┬────────┘
     │
     ▼
┌────────────────────────────┐
│ ¿i < longitud(ORACION)?    │─No─► FIN
└────┬───────────────────────┘
     │Sí
     ▼
┌─────────────────────────┐
│ c ← ORACION[i]          │
└────┬────────────────────┘
     │
     ▼
┌────────────────────┐
│ ¿c == " "?         │
└───┬───────┬────────┘
    │Sí     │No
    ▼       ▼
┌────────┐ ┌───────────┐
│ añadir │ │ añadir c  │
│ "-"    │ │ al        │
│ a res  │ │ resultado │
└──┬─────┘ └────┬──────┘
   │            │
   └────┬───────┘
        ▼
   i ← i + 1
        │
        └───► (Regresa a la pregunta del while)

"""

# c) Prueba de escritorio

"""

Supongamos la frase "yo amo python".

i	c (carácter)	resultado
0	    "y"	            "y"
1	    "o"	            "yo"
2	    " "	            "yo-"
3	    "a"	            "yo-a"
4	    "m"	            "yo-am"
5	    "o"	            "yo-amo"
6	    " "	            "yo-amo-"
7	    "p"	            "yo-amo-p"
8	    "y"	            "yo-amo-py"
9	    "t"	            "yo-amo-pyt"
10	    "h"	            "yo-amo-pyth"
11	    "o"	            "yo-amo-pytho"
12	    "n"	            "yo-amo-python"
Cuando i = 13 termina el bucle → salida correcta "yo-amo-python".

"""

# d) Implementación en Python



oracion = input("Escribe una oración: ")

resultado = ""            # aquí iremos armando la nueva frase
for caracter in oracion:  # recorremos cada letra
    if caracter == " ":
        resultado += "-"  # si es espacio, metemos un guión
    else:
        resultado += caracter  # si no, la misma letra

print("Frase convertida:", resultado)


# e) Pruebas para verificar funcionamiento

"""

Entrada: "hola mundo" → Salida esperada: "hola-mundo"
Entrada: "  espacios  al  inicio" → "--espacios--al--inicio"
Entrada: "" (cadena vacía) → ""
Entrada: "sin_espacios" → "sin_espacios" (nada cambia)

"""

# f) Uso del depurador

# Probando el ejercicio de cambiar espacios por guiones

frase1 = "hola mundo python"
resultado = ""

for caracter in frase1:
    if caracter == " ":
        resultado += "-"
    else:
        resultado += caracter

print("Prueba 1:")
print("Original:", frase1)
print("Resultado:", resultado)


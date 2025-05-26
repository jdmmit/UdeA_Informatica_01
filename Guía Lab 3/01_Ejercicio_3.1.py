# Ejercicio 3.1 - Tipo de carácter

"""
Escriba un programa que tome un carácter (es decir, un string de longitud 1) y determine si el carácter es vocal, consonante o un dígito. Además, para las vocales y consonantes determine si es mayúscula o minúscula.Test:

Entrada	Salida
a	Vocal - Minúscula
X	Consonante - Mayúscula
8	Dígito
$	-
Puede hacer uso del operador in

"""


# a) Análisis del problema
"""
Entrada:
Un solo carácter (puede ser una letra, un número o un símbolo).

Salida:

Si es una vocal, decir si es mayúscula o minúscula.
Si es una consonante, decir si es mayúscula o minúscula.
Si es un dígito, decir "Dígito".
Si no es ninguna de las anteriores, mostrar "-".

"""
# b) Algoritmo en diagrama de flujo

"""
┌──────────────┐
│   INICIO     │
└─────┬────────┘
      │
      ▼
┌────────────────────────────┐
│ Leer carácter (string de 1)│
└─────┬──────────────────────┘
      │
      ▼
┌────────────────────────────┐
│ ¿carácter es dígito?       │
└─────┬───────────────┬──────┘
      │Sí             │No
      ▼               ▼
┌─────────────┐   ┌────────────────────────────┐
│ "Dígito"    │   │ ¿carácter es vocal?        │
└─────┬───────┘   └─────┬───────────────┬──────┘
      │                │Sí              │No
      ▼                ▼                ▼
   [FIN]        ┌────────────────┐  ┌────────────────────────────┐
                │ ¿Es mayúscula? │  │ ¿carácter es consonante?   │
                └───┬─────┬──────┘  └─────┬───────────────┬──────┘
                    │Sí   │No             │Sí             │No
                    ▼     ▼               ▼               ▼
          ┌──────────────┐ ┌──────────────┐ ┌────────────────┐
          │"Vocal - May."│ │"Vocal - Min."│ │¿Es mayúscula?  │
          └─────┬────────┘ └─────┬────────┘ └───┬─────┬──────┘
                │                │              │Sí   │No
                ▼                ▼              ▼     ▼
             [FIN]            [FIN]   ┌──────────────┐ ┌──────────────┐
                                      │"Cons. - May."│ │"Cons. - Min."│
                                      └─────┬────────┘ └─────┬────────┘
                                            │                │
                                            ▼                ▼
                                         [FIN]            [FIN]
      ▼
┌─────────────┐
│     "-"     │
└─────┬───────┘
      │
     [FIN]

"""

# c) Prueba de escritorio

"""

Entrada	                Salida
    a	            Vocal - Minúscula
    X	            Consonante - Mayúscula
    8	            Dígito
    $	            -

"""

# d) Implementación en Python


caracter = input("Ingrese un caracter: ")

vocales_minus = "aeiou"
vocales_mayus = "AEIOU"
consonantes_minus = "bcdfghjklmnñpqrstvwxyz"
consonantes_mayus = "BCDFGHJKLMNÑPQRSTVWXYZ"
digitos = "0123456789"

if caracter in vocales_minus:
    print("Su caracter ingresado es Vocal - Minúscula")
elif caracter in vocales_mayus:
    print("Su caracter ingresado es Vocal - Mayúscula")
elif caracter in consonantes_minus: 
    print("Su caracter ingresado es Consonante - Minúscula")
elif caracter in consonantes_mayus:
    print("Su caracter ingresado es Consonante - Mayúscula")
elif caracter in digitos:
    print("Su caracter ingresado es Dígito")
else:
    print("-")

# e) Pruebas para verificar funcionamiento

"""

Puedes probar con los siguientes valores:

Si pones "a", sale "Vocal - Minúscula".
Si pones "X", sale "Consonante - Mayúscula".
Si pones "8", sale "Dígito".
Si pones "$", sale "-".

"""

# f) Uso del depurador

print("caracter:", caracter)
print("es vocal minúscula:", caracter in vocales_minus)
print("es vocal mayúscula:", caracter in vocales_mayus)
print("es consonante minúscula:", caracter in consonantes_minus)
print("es consonante mayúscula:", caracter in consonantes_mayus)
print("es dígito:", caracter in digitos)
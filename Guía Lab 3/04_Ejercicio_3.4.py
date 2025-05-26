# Ejercicio 3.
"""
3.4. Crea un algoritmo para ocultar mensajes. El programa debe recibir un mensaje y reorganizar los caracteres de tal forma que las letras con índices pares queden al inicio y las impares después. Por ejemplo la palabra “secreto” quedará como “sceoert” debido a los caracteres s,c,e,o corresponden a los índices 0,2,4,6, y los caracteres e,o,r,t corresponden a los índices 1,3,5. Además si el caracter es una vocal, debe cambiarla por su posición dentro de las vocales, es decir a = 1, e = 2, i = 3, o = 4, u = 5.

"""


# a) Análisis del problema
"""

Entrada:
Un mensaje (cadena), por ejemplo:"secreto"

Salida:
El mensaje oculto, donde:

Primero van los caracteres en posiciones pares (0, 2, 4, ...), luego los pares (1, 3, 5, ...).
Si un carácter es vocal (a, e, i, o, u), se reemplaza por su posición:
a=1, e=2, i=3, o=4, u=5.
Ejemplo:
Mensaje: "secreto"
Índices pares: 0(s), 2(c), 4(e), 6(o) → s, c, e, o
Índices impares: 1(e), 3(r), 5(t) → e, r, t
Reemplazando vocales:

s, c, e(2), o(4) → s, c, 2, 4
e(2), r, t → 2, r, t
Resultado:"sc242rt"

"""
# b) Algoritmo en diagrama de flujo

"""
┌──────────────┐
│   INICIO     │
└──────┬───────┘
       ▼
┌────────────────────────────┐
│   Pedir mensaje            │
└──────┬─────────────────────┘
       ▼
┌────────────────────────────┐
│ Cambiar vocales por números│
└──────┬─────────────────────┘
       ▼
┌────────────────────────────┐
│ Inicializar pares = ""     │
│ Inicializar impares = ""   │
└──────┬─────────────────────┘
       ▼
┌────────────────────────────┐
│ Recorrer cada índice i     │
│ del mensaje cambiado       │
└──────┬─────────────────────┘
       ▼
┌────────────────────────────┐
│ ¿i es par?                 │
└───┬───────────────┬────────┘
    │Sí             │No
    ▼               ▼
┌────────────┐   ┌────────────┐
│Agregar     │   │Agregar     │
│a pares     │   │a impares   │
└────┬───────┘   └────┬───────┘
     │                │
     └──────┬─────────┘
            ▼
┌────────────────────────────┐
│¿Hay más letras?            │
└──────┬─────────────────────┘
       │Sí
       ▼
   (Repetir ciclo)
       │No
       ▼
┌────────────────────────────┐
│Unir pares + impares        │
└──────┬─────────────────────┘
       ▼
┌────────────────────────────┐
│Mostrar mensaje oculto      │
└──────┬─────────────────────┘
       ▼
     [FIN]

"""

# c) Prueba de escritorio

"""
Mensaje:"secreto"

Índice	Letra	Par/Impar	¿Vocal?	    Resultado
0	  s	    Par	   No	        s (pares)
1        mi	    Impar	   Si	        2 (impares)
2	  do	    Par	   No	        c (pares)
3	  o	    Impar	   No	        r (impares)
4	  mi	    Par	   Si	        2 (pares)
5	  el	    Impar	   No	        t (impares)
6	  o	    Par	   Si	        4 (pares)
Pares: s, c, 2, 4
Impares: 2, r, t
Resultado:"sc242rt"

"""

# d) Implementación en Python

# Pide el mensaje al usuario
mensaje = input("Escribe el mensaje: ")


# Cambia las vocales por números
mensaje_cambiado = ""
for letra in mensaje:
    if letra == "a":
        mensaje_cambiado += "1"
    elif letra == "e":
        mensaje_cambiado += "2"
    elif letra == "i":
        mensaje_cambiado += "3"
    elif letra == "o":
        mensaje_cambiado += "4"
    elif letra == "u":
        mensaje_cambiado += "5"
    elif letra == "A":
        mensaje_cambiado += "1"
    elif letra == "E":
        mensaje_cambiado += "2"
    elif letra == "I":
        mensaje_cambiado += "3"
    elif letra == "O":
        mensaje_cambiado += "4"
    elif letra == "U":
        mensaje_cambiado += "5"
    else:
        mensaje_cambiado += letra
       

# Separa en pares e impares
pares = ""
impares = ""
for i in range(len(mensaje_cambiado)):
    if i % 2 == 0:
        pares += mensaje_cambiado[i]
    else:
        impares += mensaje_cambiado[i]

# Une los dos y muestra el resultado
mensaje_oculto = pares + impares
print("Mensaje oculto:", mensaje_oculto)

# e) Pruebas para verificar funcionamiento

"""

Prueba 1:
Entrada: "secreto"
Salida esperada:"sc242rt"

Prueba 2:
Entrada: "amigo"
Índices pares: 0(a=1), 2(i=3), 4(o=4) → 1, 3, 4
Índices pares: 1(m), 3(g) → m, g
Salida esperada:"134mg"

Prueba 3:
Entrada: "hola mundo"
Pares: h, l, , u(5), d
Impares: o(4), a(1), m, n, o(4)
Salida esperada:"hl 5do1mn4"

"""

# f) Uso del depurador


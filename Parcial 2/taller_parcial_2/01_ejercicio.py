"""Manejo de ciclos y condicionales
Escribe una función en Python que toma como entrada una cadena de números positivos separados por guiones y determina si cada trío de números está en orden ascendente. La función también debe devolver la suma de todos los números en la cadena. Si algún trío de números no cumple con esta condición, la función debe devolver False y la suma de los valores debe ser 0. A continuación se muestran algunos ejemplos:

Entrada: “059-359-789-456”
Salida: Verdadero, Suma: 70
Entrada: “149-694-569-459”
Salida: Falso, Suma: 0
Entrada: “789-569-479-560”
Salida: Falso, Suma: 0
Entrada: “458-589-159-489”
Salida: Verdadero, Suma: 69
Nota: Los tríos que se encuentran en rojo son los que no cumplen la condición.

La cadena de cuerdas con números positivos separados por guiones debe ser
ingresada por el usuario. Se supone que la cadena siempre contendrá 3 números
entre cada guion y que habrá exactamente 4 tríos de números en la cadena (como
se muestra en los ejemplos).
"""

def check_secuencia(secuencia_str):
    
    for trio_number in range(4):
        suma = 0
        ini = 0
        end = 3 
        trio = secuencia_str[ini:end]
        if (int(trio[0]) <= int(trio[1])) and (int(trio[1])) <= (int(trio[2])):
            suma_trio = int(trio[0]) + int(trio[1]) + int(trio[2])
            suma += suma_trio
        else:
            return False, 0
        
        ini = ini + 4
        end = end + 4
        
    return True, suma

secuencia_str = input("Ingrese la secuencia: ")
salida, suma = check_secuencia(secuencia_str)
print(f"Salida: {salida}, Suma: {suma}")
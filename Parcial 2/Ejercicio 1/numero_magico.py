# ========== Ejercicio 1 ==========
# ========== Juan David Murillo Mejia ==========


def numero_magico(numero):
    
    suma_primera = int(numero[0]) + int(numero[1]) + int(numero[2])
    suma_segunda = int(numero[3]) + int(numero[4]) + int(numero[5])
    
    for digito in numero:
        if int(digito) % 2 != 0:
            return False
        
    if suma_primera == suma_segunda:
        return True
    else:
        return False


# prueba del ejercico.    
print(numero_magico("426840"))  # True
print(numero_magico("248620"))  # False # no cumple la suma
print(numero_magico("248613"))  # False # tiene digitos impares

numero = input("Ingrese un numero de 6 digitos: ")
print(numero_magico(numero))
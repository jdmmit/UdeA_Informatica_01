# Ejercicio 3.
"""
3.3. Se necesita verificar la seguridad de una contraseña siguiendo las siguientes condiciones:
●	Su longitud debe estar entre 8 y 20 caracteres.
●	Debe incluir letras, números.
●	Debe incluir al menos uno de los siguientes caracteres especiales:
!, ”, #, $, %, &, /, (, ), =, ?, +, * ● No debe ser palíndroma.
Finalmente debe indicar en pantalla si ha cumplido los requisitos de forma individual.


"""


# a) Análisis del problema
"""
Datos de Entrada:

Una contraseña (texto)
Datos de Salida:

Mensajes de verificación para cada regla:
Longitud (8-20 caracteres)
Si tiene letras y números
Si tiene caracteres especiales
Si no es palíndromo
Mensaje final (si es segura o no)

"""
# b) Algoritmo en diagrama de flujo

"""
┌─────────────┐
│   INICIO    │
└──────┬──────┘
       ▼
┌──────────────────┐
│Pedir contraseña  │
└──────┬───────────┘
       ▼
┌──────────────────┐
│Revisar longitud  │───►Mostrar resultado
└──────┬───────────┘
       ▼
┌──────────────────┐
│Buscar letras y   │───►Mostrar resultado
│    números       │
└──────┬───────────┘
       ▼
┌──────────────────┐
│Buscar caracteres │───►Mostrar resultado
│   especiales     │
└──────┬───────────┘
       ▼
┌──────────────────┐
│Revisar si es     │───►Mostrar resultado
│   palíndromo     │
└──────┬───────────┘
       ▼
┌──────────────────┐
│ Mensaje final    │
└──────┬───────────┘
       ▼
     [FIN]

"""

# c) Prueba de escritorio

"""

Probemos con la contraseña: "Hola123!"

Paso	                        Operación	                                Resultado
1. Longitud	                  len("Hola123!") = 8                       ✓ (8 ≥ 8 y ≤ 20)
2. Letras y números	          H,o,l,a = letras;1,2,3 = números          ✓ (tiene ambos)
3. Caracteres especiales	  ! = especial	                            ✓ (tiene !)
4. Palíndromo	              "Hola123!" ≠ "!321aloH"                   ✓ (no es palíndromo)

"""

# d) Implementación en Python

# Verificador de contraseñas simple



# 1. Pedir la contraseña

contraseña = input("Escribe tu contraseña: ")

# 2. Revisar longitud

if len(contraseña) >= 8 and len(contraseña) <= 20:
    print("✓ La longitud está bien")
else:
    print("✗ La longitud debe estar entre 8 y 20 caracteres")

# 3. Buscar letras y números

tiene_letra = False
tiene_numero = False

for caracter in contraseña:
    if caracter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        tiene_letra = True
    if caracter in "0123456789":
        tiene_numero = True

if tiene_letra and tiene_numero:
    print("✓ Tiene letras y números")
else:
    print("✗ Debe tener letras y números")

# 4. Buscar caracteres especiales

caracteres_especiales = "!\"#$%&/()=?+*"
tiene_especial = False

for caracter in contraseña:
    if caracter in caracteres_especiales:
        tiene_especial = True
        break

if tiene_especial:
    print("✓ Tiene caracteres especiales")
else:
    print("✗ Debe tener caracteres especiales")

# 5. Revisar si es palíndromo

contraseña_alreves = contraseña[::-1]

if contraseña != contraseña_alreves:
    print("✓ No es palíndromo")
else:
    print("✗ No debe ser palíndromo")

# 6. Mensaje final

print("\n--- Resultado final ---")
if (len(contraseña) >= 8 and len(contraseña) <= 20 and
    tiene_letra and tiene_numero and
    tiene_especial and contraseña != contraseña_alreves):
    print("¡Tu contraseña es segura! ")
else:
    print("Tu contraseña no cumple todos los requisitos ")

# e) Pruebas para verificar funcionamiento



# Casos de prueba simples
contraseñas_prueba = [
    "abc",          # Muy corta
    "Hola123!",     # Cumple todo
    "12345678",     # Solo números
    "ana12321",     # Palíndromo
    "MiPass2024#"   # Cumple todo
]

# Probar cada contraseña
for prueba in contraseñas_prueba:
    print(f"\nProbando contraseña: {prueba}")
    # Aquí va el código anterior
    contraseña = prueba
    # ... (resto del código)



# f) Uso del depurador

"""
Problema: Espacios en blanco
Solución: Agregar contraseña = contraseña.strip()
Problema: Contraseña vacía
Solución: Agregar al inicio:
"""

if contraseña == "":
    print("La contraseña no puede estar vacía")
    exit()

"""
Problema: Mayúsculas en palíndromos
Solución: Usar contraseña.lower() para la comparación
Problema: Caracteres no contemplados
Solución: Agregar más caracteres a la lista de especiales

"""
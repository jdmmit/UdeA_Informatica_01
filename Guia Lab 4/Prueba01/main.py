import ahorcado

# Juego del ahorcado
print("¡Bienvenido al Juego del Ahorcado!")
print("Instrucciones:")
print("1. Tienes 8 intentos para adivinar la palabra")
print("2. Puedes ingresar una letra a la vez")
print("3. Si fallas, perderás un intento")
print("4. Si adivinas la palabra, ¡ganas!\n")

# Despliegue de la entrada
ahorcado.printIntro('intro.txt')

# Variables globales
letrasIntentadas = ''
numeroIntentos = 8
otraVez = 'y'
palabras_jugadas = 0
palabras_adivinadas = 0

while otraVez == 'y':
    '''Inicio ciclo de nuevo juego'''
    # Selección del modo de juego
    print("\n=== SELECCIONA EL MODO DE JUEGO ===")
    print("1. Ingresar palabra secreta manualmente")
    print("2. Palabra aleatoria desde archivo")
    modo = input("Elige el modo (1/2): ").strip()

    # Obtener palabra según el modo
    if modo == '1':
        palabraSecreta = ahorcado.inputSecret()
    else:
        contenido = ahorcado.loadWords("superHeroes.txt")
        palabraSecreta = ahorcado.pickWord(contenido, ',')

    palabras_jugadas += 1
    ban = 1  # Bandera de juego activo
    letrasIntentadas = ''  # Reiniciamos letras intentadas
    numeroIntentos = 8    # Reiniciamos intentos

    while ban == 1:
        '''Inicio ciclo para adivinar la palabra oculta'''
        # Mostrar estado actual del juego
        print("\n" + "="*40)
        print(f"Intentos restantes: {numeroIntentos}")
        print("Letras disponibles:", ahorcado.obtenerLetrasDisponibles(letrasIntentadas))
        print("\nPalabra:", ahorcado.obtenerParteAdivinada(palabraSecreta, letrasIntentadas))

        # Solicitar letra al jugador
        letra = input("\nIngresa una letra: ").lower()

        # Validar entrada
        if len(letra) != 1:
            print("Por favor, ingresa una sola letra.")
            continue

        # Verificar si la letra ya fue intentada
        if ahorcado.verificarLetraIngresada(letra, letrasIntentadas):
            print("¡Ya usaste esa letra! Intenta con otra.")
            continue

        # Agregar letra a intentadas
        letrasIntentadas += letra

        # Verificar si la letra está en la palabra
        if letra in palabraSecreta.lower():
            print("¡Bien! La letra está en la palabra.")

            # Verificar si ganó
            if ahorcado.palabraAdivinada(palabraSecreta, letrasIntentadas):
                print("\n¡FELICITACIONES! ¡Has ganado!")
                print(f"La palabra era: {palabraSecreta}")
                palabras_adivinadas += 1
                ban = 0  # Terminar el juego
        else:
            print("¡Ups! Esa letra no está en la palabra.")
            numeroIntentos -= 1

        # Verificar si perdió
        if numeroIntentos == 0:
            print("\n¡Lo siento! Te has quedado sin intentos.")
            print(f"La palabra era: {palabraSecreta}")
            ban = 0  # Terminar el juego

    # Mostrar estadísticas
    print("\n=== ESTADÍSTICAS ===")
    print(f"Palabras jugadas: {palabras_jugadas}")
    print(f"Palabras adivinadas: {palabras_adivinadas}")
    print(f"Porcentaje de éxito: {(palabras_adivinadas/palabras_jugadas)*100:.1f}%")

    # Solicitud de nuevo juego
    otraVez = input('\n¿Desea jugar otra vez? (y/n): ').lower()

print("\n¡Gracias por jugar al Ahorcado!")
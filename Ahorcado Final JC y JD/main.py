import ahorcado

# Juego del ahorcado

print("¡Bienvenido al juego del ahorcado!")
print("Instrucciones:")
print("1. Tienes 8 intentos para adivinar la palabra.")
print("2. Puedes ingresar una letra a la vez.")
print("3. si fallas, perderás un intento.")
print("4. si adivinas la palabra, ¡Ganas!. \n")

# Despliega de la entrada
ahorcado.printIntro("intro.txt")

# Variables globales
letrasIntentadas = ""
numeroIntentos = 0  # Comenzamos desde 0 para el primer dibujo
otraVez = "s"
palabras_jugadas = 0
palabras_adivinadas = 0

while otraVez == "s":
    '''Inicio ciclo de nuevo juego'''
    # Selección del modo de juego
    print("\n === Selecciona el modo de juego: ===")
    print("1. Ingresa la palabra secreta manualmente")
    print("2. Selecciona una palabra secreta al azar")
    modo = input("Selecciona el modo de juego (1 o 2): ").strip()

    # Obtener palabra según el modo
    if modo == '1':
        palabraSecreta = ahorcado.inputSecret()
    elif modo == '2':
        contenido = ahorcado.loadWords("superHeroes.txt")
        palabraSecreta = ahorcado.pickWord(contenido, ',')
    else:
        print("Opción no válida. Seleccionando modo 2 por defecto.")
        contenido = ahorcado.loadWords("superHeroes.txt")
        palabraSecreta = ahorcado.pickWord(contenido, ',')

    palabras_jugadas += 1
    ban = 1 # Bandera de juego activo
    letrasIntentadas = "" # Reiniciar letras intentadas
    numeroIntentos = 0 # Reiniciar intentos

    while ban == 1:
        '''Inicio ciclo para adivinar la palabra oculta'''
        # Mostrar el dibujo del ahorcado actual
        print("\n" + ahorcado.dibujarAhorcado(numeroIntentos))

        # Mostrar estado actual del juego
        print("\n" + "="*40)
        print(f"Intentos fallidos: {numeroIntentos}")
        print("Intentos restantes:", 7 - numeroIntentos)
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

        # Verificar si la letra está en la palabra secreta
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
            numeroIntentos += 1  # Incrementamos los intentos fallidos

            # Verificar si perdió
            if numeroIntentos >= 7:
                print("\n" + ahorcado.dibujarAhorcado(numeroIntentos))
                print("\n¡Lo siento! Te has quedado sin intentos.")
                print(f"La palabra era: {palabraSecreta}")
                ban = 0  # Terminar el juego

        # Mostrar estadísticas
        if ban == 0:  # Solo mostrar estadísticas al terminar el juego
            print("\n=== ESTADÍSTICAS ===")
            print(f"Palabras jugadas: {palabras_jugadas}")
            print(f"Palabras adivinadas: {palabras_adivinadas}")
            print(f"Porcentaje de éxito: {(palabras_adivinadas/palabras_jugadas)*100:.1f}%")

    # Solicitud de nuevo juego
    otraVez = input('\n¿Desea jugar otra vez? (s/n): ').lower()

print("\n¡Gracias por jugar al Ahorcado!")
import ahorcado
import os
import time

def main():
    # Variables del juego
    letrasIntentadas = []
    numeroIntentos = 7  # 7 intentos para coincidir con los dibujos
    palabraSecreta = ""
    otraVez = True
    palabras_jugadas = 0
    palabras_adivinadas = 0

    # Mostrar intro
    ahorcado.printIntro("intro.txt")
    input("\nPresiona Enter para continuar...")

    while otraVez:
        ahorcado.limpiarPantalla()
        print("\n=== MODO DE JUEGO ===")
        print("1. Ingresar palabra secreta")
        print("2. Palabra aleatoria de superhéroes")
        modo = input("\nElige el modo de juego (1/2): ").strip()

        if modo == "1":
            ahorcado.limpiarPantalla()
            palabraSecreta = ahorcado.inputSecret()
        else:
            palabras = ahorcado.loadWords("superHeroes.txt")
            palabraSecreta = ahorcado.pickWord(palabras)

        letrasIntentadas = []
        numeroIntentos = 7
        palabras_jugadas += 1
        ahorcado.limpiarPantalla()

        while numeroIntentos >= 0:
            print("\n=== AHORCADO ===")
            print(ahorcado.dibujarAhorcado(numeroIntentos))
            print("\nPalabra:", ahorcado.obtenerParteAdivinada(palabraSecreta, letrasIntentadas))
            print(f"Intentos restantes: {numeroIntentos}")
            print("Letras disponibles:", ahorcado.obtenerLetrasDisponibles(letrasIntentadas))

            if numeroIntentos == 0:
                print("\n¡GAME OVER! Te quedaste sin intentos.")
                print("La palabra era:", palabraSecreta)
                break

            letra = input("\nIngresa una letra: ").lower().strip()

            if len(letra) != 1 or not letra.isalpha():
                print("\n¡Por favor, ingresa una sola letra!")
                time.sleep(1)
                ahorcado.limpiarPantalla()
                continue

            if ahorcado.verificarLetraIngresada(letra, letrasIntentadas):
                print("\n¡Ya intentaste esa letra! Prueba con otra.")
                time.sleep(1)
                ahorcado.limpiarPantalla()
                continue

            letrasIntentadas.append(letra)

            if letra in palabraSecreta:
                print("\n¡Correcto! La letra está en la palabra.")
                if ahorcado.palabraAdivinada(palabraSecreta, letrasIntentadas):
                    ahorcado.limpiarPantalla()
                    print("\n¡FELICITACIONES! ¡Ganaste!")
                    print("La palabra era:", palabraSecreta)
                    print(ahorcado.dibujarAhorcado(numeroIntentos))
                    palabras_adivinadas += 1
                    break
            else:
                print("\n¡Incorrecto! La letra no está en la palabra.")
                numeroIntentos -= 1

            time.sleep(1)
            ahorcado.limpiarPantalla()

        print(f"\nPalabras jugadas: {palabras_jugadas}")
        print(f"Palabras adivinadas: {palabras_adivinadas}")

        respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower().strip()
        otraVez = respuesta == 's'

    print("\n¡Gracias por jugar!")

if __name__ == "__main__":
    main()

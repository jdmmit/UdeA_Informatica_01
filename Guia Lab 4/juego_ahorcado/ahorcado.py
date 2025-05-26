import random
import string
import os

def printIntro(nombre_archivo):
    """Imprime el mensaje de bienvenida desde un archivo"""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")

def inputSecret():
    """Solicita al usuario que ingrese una palabra secreta"""
    print("\nJugador 1, ingresa la palabra secreta: ")
    return input().lower()

def loadWords(nombre_archivo):
    """Carga las palabras desde un archivo"""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        return ""

def countWords(cadena_palabras):
    """Cuenta el número de palabras en una cadena"""
    return len(cadena_palabras.split(','))

def pickWord(cadena_palabras):
    """Selecciona una palabra aleatoria"""
    palabras = cadena_palabras.split(',')
    return random.choice(palabras).strip()

def obtenerParteAdivinada(palabra_secreta, letras_intentadas):
    """Muestra la palabra con las letras adivinadas"""
    resultado = ''
    for letra in palabra_secreta:
        if letra in letras_intentadas:
            resultado += letra + ' '
        elif letra == ' ':
            resultado += '  '
        else:
            resultado += '_ '
    return resultado.strip()

def obtenerLetrasDisponibles(letras_intentadas):
    """Muestra las letras que aún no se han usado"""
    return ''.join(letra for letra in string.ascii_lowercase 
                  if letra not in letras_intentadas)

def verificarLetraIngresada(letra, letras_intentadas):
    """Verifica si una letra ya fue intentada"""
    return letra in letras_intentadas

def palabraAdivinada(palabra_secreta, letras_intentadas):
    """Verifica si la palabra ha sido adivinada"""
    return all(letra in letras_intentadas or letra == ' ' 
              for letra in palabra_secreta)

def dibujarAhorcado(intentos):
    """Dibuja el estado actual del ahorcado"""
    AHORCADO = ["""
      +---+
      |   |
          |
          |
          |
          |
    ==========""", """
      +---+
      |   |
      O   |
          |
          |
          |
    ==========""", """
      +---+
      |   |
      O   |
      |   |
          |
          |
    ==========""", """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    ==========""", """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    ==========""", """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    ==========""", """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    ==========""", """
      +---+
      |   |
     [O]  |
     /|\  |
     / \  |
          |
    =========="""]
    return AHORCADO[7 - intentos]

def limpiarPantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

import random
import string
import os

def printIntro(fileName):
    """Imprime el contenido del archivo de bienvenida"""
    try:
        with open(fileName, 'r', encoding='utf-8') as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print("Error: No se encontró el archivo de introducción")

def inputSecret():
    """Solicita y retorna la palabra secreta"""
    pSec = input("Ingrese la palabra o frase oculta: ").lower()
    # Limpiamos pantalla para que el otro jugador no vea
    os.system('cls' if os.name == 'nt' else 'clear')
    return pSec

def loadWords(fileName):
    """Carga las palabras desde un archivo"""
    try:
        with open(fileName, 'r', encoding='utf-8') as archivo:
            palabras = archivo.read().strip()
        return palabras
    except FileNotFoundError:
        return "python,programacion,computadora"  # palabras por defecto

def countWords(palabras, separador):
    """Cuenta el número de palabras en la cadena"""
    if not palabras:  # Si está vacío
        return 0
    # Dividimos por el separador y contamos elementos no vacíos
    conta = len([p for p in palabras.split(separador) if p.strip()])
    return conta

def pickWord(palabras, separador):
    """Selecciona una palabra aleatoria de la lista"""
    # Convertimos la cadena en lista
    lista_palabras = [p.strip() for p in palabras.split(separador) if p.strip()]
    if not lista_palabras:  # Si la lista está vacía
        return "python"
    # Seleccionamos palabra aleatoria
    palabra = random.choice(lista_palabras)
    return palabra.lower()

def obtenerParteAdivinada(palabraSecreta, letrasIntentadas):
    """Muestra el progreso de la palabra con guiones"""
    pPrint = ''
    for letra in palabraSecreta:
        if letra == ' ':
            pPrint += ' '
        elif letra.lower() in letrasIntentadas:
            pPrint += letra
        else:
            pPrint += '_'
    return ' '.join(pPrint)

def obtenerLetrasDisponibles(letrasIntentadas):
    """Muestra las letras que aún no se han usado"""
    # Obtenemos todas las letras del alfabeto
    alfabeto = string.ascii_lowercase
    # Filtramos las letras que no están en letrasIntentadas
    resto = ''.join([letra for letra in alfabeto if letra not in letrasIntentadas])
    return resto

def verificarLetraIngresada(letra, letrasIntentadas):
    """Verifica si una letra ya fue intentada"""
    return letra.lower() in letrasIntentadas

def palabraAdivinada(palabra, letrasIntentadas):
    """Verifica si todas las letras de la palabra han sido adivinadas"""
    for letra in palabra:
        if letra != ' ' and letra.lower() not in letrasIntentadas:
            return False
    return True


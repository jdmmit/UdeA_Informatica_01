import ahorcado
# Juego de ahorcado

# Introduzca aquí las instrucciones para el juego

# Despliegue de la entrada
printIntro('intro.txt')

# Variables globales
letrasIntentadas=''
numeroIntentos = 8
otraVez = 'y'

while otraVez == 'y':
	''' Inicio ciclo de nuevo juego '''
	# Selección del modo de juego (1: palabra secreta, 2: archivo)
	# Código ...
	
	# ...
	ban = 1 # Bandera que indica la culminación de una tanda de turnos
			# ya sea por que el usuario acierta o por que pierde
			
	# Impresión de las estadísticas (Numero de intentos, letras disponibles, palabra secreta (rayas))
	# Código ...
	
	# ...
	while ban == 1:
		''' Inicio ciclo para adivinar la palabra oculta '''
		# Solicitud interactiva de palabras
		# Código ...
		
		# ...
		
		# Verificación de la letra e impresión de lo que va de la palabra
		# Código ...
		
		# ...
		
		# Verificación de la condición de finalización del juego
		# Código ...
		
		# ...
		
		# Impresión del estado del juego (Número de intentos, letras disponibles)
		# Código ...
		
		# ...
		
		# Verificación de la condición de finalización del juego
		# Código ...
		
		# ...
		''' Fin ciclo para adivinar la palabra oculta '''
	# Inicializar nuevamente las variables que crea necesario...
		
	# Solicitud de nuevo juego
	otraVez = input('Desea jugar otra vez (y/n): ')  
	otraVez = otraVez.lower()
	''' Fin ciclo de nuevo juego '''
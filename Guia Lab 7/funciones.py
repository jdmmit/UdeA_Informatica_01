"""

FUNCIONES.PY - Lab 7 Estadísticas Estudiantes 
Contiene todas las funciones para el procesamiento de datos
Autor: Juan David Murillo & Juan Camilo Medina

"""

import numpy as np
import matplotlib.pyplot as plt

# ================= VARIABLES GLOBALES =================

cursos = []
estudiantes = []
notas_matriz = []

# ================= FUNCIÓN DE GRÁFICAS =================
def plot_data(data, regression_line, years):

    """
    Grafica los datos y la Regresión Lineal
    Parámetros:
        data (list): Lista bidimensional con datos históricos [[año, estudiantes]...]
        regression_line(list): Lista de los valores y para la regresión lineal
        years(list): Lista de años entre 1980 y el año de predicción
    """

    data = np.array(data)

    plt.figure(figsize=(12, 8))
    plt.plot(data[:, 0], data[:, 1], 'bo', markersize=8, label='Datos Históricos')
    plt.plot(years, regression_line, 'r-', linewidth=2, label='Regresión Lineal')
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    plt.title('Datos Históricos y Regresión Lineal - Estudiantes Matriculados', fontsize=14, fontweight='bold')
    plt.xlabel('Año', fontsize=14, fontweight='bold')
    plt.ylabel('Número de Estudiantes', fontsize=14, fontweight='bold')

    # Añadir punto de predicción si existe
    if len(years) > len(data):
        ultimo_año = years[-1]
        ultimo_valor = regression_line[-1]
        plt.plot(ultimo_año, ultimo_valor, 'go', markersize=12, label=f'Predicción {ultimo_año}')
        plt.legend(fontsize=12)

    plt.tight_layout()
    plt.show()


def graficar_promedios(indices_promedios):

    """
    Genera un gráfico de barras con los promedios de estudiantes ordenados
    """

    global estudiantes

    # Preparar datos para el gráfico
    nombres = [estudiantes[i] for i, _ in indices_promedios] 
    promedios = [promedio for _, promedio in indices_promedios]

    # Crear el gráfico
    plt.figure(figsize=(14, 8))

    # Crear barras con colores degradados
    colores = plt.get_cmap('viridis')(np.linspace(0, 1, len(promedios)))
    barras = plt.bar(range(len(nombres)), promedios, color=colores, alpha=0.8, edgecolor='black', linewidth=0.5)

    # Personalizar el gráfico
    plt.title(' Promedios de Estudiantes (Ordenamiento Burbuja)', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Estudiantes', fontsize=12, fontweight='bold')
    plt.ylabel('Promedio de Notas', fontsize=12, fontweight='bold')
    plt.xticks(range(len(nombres)), nombres, rotation=45, ha='right')

    # Añadir valores encima de las barras
    for i, (barra, promedio) in enumerate(zip(barras, promedios)):
        plt.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.05, 
                f'{promedio:.2f}', ha='center', va='bottom', fontweight='bold', fontsize=10)

    # Añadir línea de promedio general
    promedio_general = sum(promedios) / len(promedios)
    plt.axhline(y=promedio_general, color='red', linestyle='--', alpha=0.7, 
                label=f'Promedio General: {promedio_general:.2f}')

    plt.grid(True, axis='y', alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


def graficar_cantidad_cursos(indices_cursos):

    """
    Genera un gráfico de barras con la cantidad de cursos por estudiante
    """

    global estudiantes

    # Preparar datos para el gráfico
    nombres = [estudiantes[i] for i, _ in indices_cursos]
    cantidades = [cantidad for _, cantidad in indices_cursos]

    # Crear el gráfico
    plt.figure(figsize=(14, 8))

    # Crear barras con colores según la cantidad
    colores = ['#2E8B57' if c == max(cantidades) else '#4169E1' if c >= 4 else '#FF6347' for c in cantidades]
    barras = plt.bar(range(len(nombres)), cantidades, color=colores, alpha=0.8, edgecolor='black', linewidth=0.5)

    # Personalizar el gráfico
    plt.title('Cantidad de Cursos por Estudiante (Ordenamiento Selección)', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Estudiantes', fontsize=12, fontweight='bold')
    plt.ylabel('Número de Cursos', fontsize=12, fontweight='bold')
    plt.xticks(range(len(nombres)), nombres, rotation=45, ha='right')

    # Añadir valores encima de las barras
    for i, (barra, cantidad) in enumerate(zip(barras, cantidades)):
        plt.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.05, 
                f'{cantidad}', ha='center', va='bottom', fontweight='bold', fontsize=12)

    # Añadir línea del máximo de cursos posibles
    max_cursos = len(cursos)
    plt.axhline(y=max_cursos, color='red', linestyle='--', alpha=0.7, 
                label=f'Máximo posible: {max_cursos} cursos')

    # Configurar eje Y para mostrar solo números enteros
    plt.ylim(0, max_cursos + 0.5)
    plt.yticks(range(0, max_cursos + 1))

    plt.grid(True, axis='y', alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

# ================= PARTE 1: GESTIÓN DE NOTAS =================

def cargar_datos():

    """
    Carga los datos desde el archivo notas_estudiantes.csv
    """

    global cursos, estudiantes, notas_matriz

    try:
        with open("notas_estudiantes.csv", "r") as archivo:
            lineas = archivo.readlines()

        # Primera linea: codigos de cursos
        cursos = [curso.strip() for curso in lineas[0].strip().split(",")]

        # Segunda linea: documentos de estudiantes
        estudiantes = [est.strip() for est in lineas[1].strip().split(",")]

        # Resto de lineas: notas
        notas_matriz = []
        for i in range(2, len(lineas)):
            if lineas[i].strip(): # Verificar que la línea no esté vacía
                fila = lineas[i].strip().split(",")
                notas_fila = []

                for nota in fila:
                    try:
                        notas_fila.append(float(nota.strip()))
                    except ValueError:
                        notas_fila.appennd(-1) # Por si hay datos inválidos
                notas_matriz.append(notas_fila)

        print("✓ Datos cargados exitosamente!")
        print(f" Cursos: {len(cursos)}")
        print(f" Estudiantes: {len(estudiantes)}")
        print(f" Matriz de notas: {len(notas_matriz)} filas")
        

        return True
    
    except FileNotFoundError:
        print(" Error: No se encontró el archivo 'notas_estudiantes.csv'")
        print(" Asegúrate de que el archivo esté en la misma carpeta que este programa")
        return False
    except Exception as e:
        print(f" Error al cargar datos: {e}")
        return False
        

def eliminar_estudiante():

    """
    Elimina un estudiante por su documento
    """

    global estudiantes, notas_matriz

    if not estudiantes:
        print(" No hay datos cargados. Use la opción 1 primero.")
        return

    print(" \n Estudiantes disponibles: \n ")
    for i, est in enumerate(estudiantes):
        print(f"  {i+1}. {est}")

    documento = input("\nIngrese el documento del estudiante a eliminar: ").strip()

    try:
        indice = estudiantes.index(documento)
        estudiante_eliminado = estudiantes.pop(indice)
        notas_matriz.pop(indice)
        print(f" Estudiante {estudiante_eliminado} eliminado exitosamente ")
    except ValueError:
        print(" Estudiante no encontrado. Verifique el documento. ")


def mayor_nota_estudiante():

    """
    Encuentra la mayor nota de un estudiante
    """
    
    global estudiantes, cursos, notas_matriz

    if not estudiantes:
        print(" No hay datos cargados. Use la opcion 1 primero. ")
        return
    
    print(" \n Estudiantes disponibles: \n ")

    for i, est in enumerate(estudiantes):
        print(f" {i + 1}. {est}")

    documento = input(" \n Ingresa el documento del estudiante: \n ")

    try:
        indice = estudiantes.index(documento)
        notas_estudiante = notas_matriz[indice]

        mayor_nota = -3
        curso_mayor = ""

        print(f"\n📊 Notas del estudiante {documento}:")
        for i, nota in enumerate(notas_estudiante):
            if nota >= 0:
                print(f"  {cursos[i]}: {nota}")
                if nota > mayor_nota:
                    mayor_nota = nota
                    curso_mayor = cursos[i]
            elif nota == -1:
                print(f"  {cursos[i]}: CANCELADO")
            elif nota == -2:
                print(f"  {cursos[i]}: NO MATRICULADO")
        
        if mayor_nota >= 0:
            print(f"\n Mayor nota: {mayor_nota} en el curso {curso_mayor} \n")
        else:
            print("\n El estudiante no tiene notas válidas \n ")

    except ValueError:
        print(" Estudiante no encontrado. Verifique el documento. ")
        
        
def calcular_promedio_estudiante(indice):
    
    """
    Calcula el promedio de un estudiante (solo notas válidas >= 0)
    """
    
    if indice >= len(notas_matriz):
        return 0
    
    notas_validas = [nota for nota in notas_matriz[indice] if nota >= 0]
    if notas_validas:
        return sum(notas_validas) / len(notas_validas)
    return


def ordenar_promedios_burbuja():
    
    """
    Ordena estudiantes por promedio usando algoritmo burbuja
    """
    
    global estudiantes, notas_matriz
    
    if not estudiantes:
        print(" No hay datos cargados. Use la opcion 1 primero. ")
        return
    
    print(" Ordenar por promedio usando Algoritmo Burbuja... ")
    
    # Crear lista de índices con sus promedios
    indices_promedios = []
    for i in range(len(estudiantes)):
        promedio = calcular_promedio_estudiante(i)
        indices_promedios.append((i, promedio))
        
    # ALGORITMO BURBUJA (requisito obligatorio del lab)
    n = len(indices_promedios)
    comparaciones = 0
    intercambios = 0
    
    for i in range(n):
        for j in range(0, n-i-1):
            comparaciones += 1
            if indices_promedios[j][1] < indices_promedios[j + 1][1]: # Mayor a menor
                indices_promedios[j], indices_promedios[j + 1] = indices_promedios[j + 1], indices_promedios[j]
                intercambios += 1
                
    # Mostrar resultados
    print(f" \n Estudiantes ordenados por promedio (mayor a menor): \n ")
    print("\n" + "-"*65 + "\n")
    
    for pos, (i, promedio) in enumerate(indices_promedios):
        print(f" {pos+1:2d}. {estudiantes[i]:12s} → Promedio: {promedio:5.2f}")
        
        print(f"\n Estadísticas del algoritmo burbuja: \n")
    print(f"  Comparaciones: {comparaciones}")
    print(f"  Intercambios: {intercambios}")

    # GENERAR GRÁFICO
    print("\n Generando gráfico de promedios... \n ")
    graficar_promedios(indices_promedios)


def contar_cursos_estudiante(indice):
    
    """
    Cuenta cuántos cursos ha cursado un estudiante (notas >= 0)
    """
    
    if indice >= len(notas_matriz):
        return 0
    return len([nota for nota in notas_matriz[indice] if nota >= 0])


def ordenar_cantidad_cursos_seleccion():
    
    """
    Ordena estudiantes por cantidad de cursos usando algoritmo selección
    """
    
    global estudiantes, notas_matriz
    
    if not estudiantes:
        print(" No hay datos cargados. Use la opción 1 primero. ")
        return

    print(" Ordenando por cantidad de cursos usando algoritmo SELECCIÓN... ")
    
    # Crear lista de índices con cantidad de cursos
    indices_cursos = []
    for i in range(len(estudiantes)):
        cantidad = contar_cursos_estudiante(i)
        indices_cursos.append((i, cantidad))
        
    # ALGORITMO DE SELECCIÓN (requisito obligatorio del lab)
    n = len(indices_cursos)
    comparaciones = 0
    intercambios = 0
    
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            comparaciones += 1
            if indices_cursos[j][1] > indices_cursos[max_idx][1]:
                max_idx = j
        if max_idx != i:
            indices_cursos[i], indices_cursos[max_idx] = indices_cursos[max_idx], indices_cursos[i]
            intercambios += 1
            
    # Mostrar resultados
    print(f"\n Estudiantes ordenados por cantidad de cursos: \n ")
    print("\n" + "-"*65 + "\n")
    for pos, (i, cantidad) in enumerate(indices_cursos):
        print(f"  {pos+1:2d}. {estudiantes[i]:12s} → {cantidad} cursos")

    print(f"\n Estadísticas del algoritmo selección: \n ")
    print(f"  Comparaciones: {comparaciones} ")
    print(f"  Intercambios: {intercambios} ")

    # GENERAR GRÁFICO
    print("\n Generando gráfico de cantidad de cursos... \n ")
    graficar_cantidad_cursos(indices_cursos)


# ================= PARTE 2: REGRESIÓN LINEAL =================


def cargar_datos_historicos():
    
    """
    Carga los datos históricos desde hist_matriculados.csv
    """
    
    años = []
    estudiantes_hist = []
    
    try:
        with open("hist_matriculados.csv", "r") as archivo:
            lineas = archivo.readlines()
            
        # Saltar encabezados y procesar datos
        for i in range(1, len(lineas)):
            linea = lineas[i].strip()
            if ',' in linea and linea:
                partes = linea.split(',')
                if len(partes) >= 2:
                    try:
                        año = int(partes[0].strip())
                        estudiantes = int(partes[1].strip())
                        años.append(año)
                        estudiantes_hist.append(estudiantes)
                    except ValueError:
                        continue

        return años, estudiantes_hist
    
    except FileNotFoundError:
        print(" Error: No se encontro el archivo 'hist_matriculados.csv'")
        return [], []
    except Exception as e:
        print(f"Error al cargar datos historicos: {e}")
        return [], []
    
    
def calcular_regrecion_lineal(años, a, b):
    
    """
    Calcula los valores de y para la regresión lineal y = ax + b
    """
    
    return [a * año + b for año in años]


def calcular_mae(valores_reales, valores_predichos):
    
    """
    Calcula el Mean Absolute Error (MAE)
    """
    
    if len(valores_reales) != len(valores_predichos):
        return float("inf")
    
    errores = [abs(valores_reales[i] - valores_predichos[i]) for i in range(len(valores_reales))]
    return sum(errores) / len(errores)


def predecir_estudiantes():
    
    """
    Función principal para predecir estudiantes matriculados
    """
    
    print("\n" + "="*60 + "\n")
    print(" PREDICCIÓN DE ESTUDIANTES MATRICULADOS ")
    print("\n" + "="*60 + "\n")
    
    # Cargar datos históricos
    años, estudiantes_hist = cargar_datos_historicos()
    
    if not años:
        print(" No se pudieron cargar los datos historicos ")
        return
    
    print(f" Datos históricos cargados: {len(años)} registros")
    print(f" Período: {min(años)} - {max(años)}")
    print(f" Rango de estudiantes: {min(estudiantes_hist)} - {max(estudiantes_hist)}")

    # Buscar mejores parámetros por tanteo (como requiere el lab)
    print(f" \n Buscando mejores parámetros por tanteo... \n")

    mejor_a = 0
    mejor_b = 0
    mejor_mae = float('inf')
    intentos = 0
    
    # Tanteo sistemático con rango amplio
    valores_a = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
    valores_b = [-5000, -4500, -4000, -3500, -3000, -2500, -2000, -1500, -1000, -500, 0]
    
    for a in valores_a:
        for b in valores_b:
            regresion = calcular_regrecion_lineal(años, a, b)
            mae = calcular_mae(estudiantes_hist, regresion)
            intentos += 1
            
            if mae < mejor_mae:
                mejor_mae = mae
                mejor_a = a
                mejor_b = b
                print(f" Nuevo mejor resultado: a={a}, b={b}, MAE={mae:.2f}")
                
    print(f" \n Resultado del tanteo: \n ")
    print(f" Intentos realizados: {intentos} ")
    print(f" Mejores parámetros: a = {mejor_a}, b = {mejor_b} ")
    print(f" Error mínimo (MAE): {mejor_mae:.2f} estudiantes ")

    # Solicitar año para predicción
    while True:
        try:
            año_pred = input(f" Ingresa el año para predecir )ej: 2030: ").strip()
            año_prediccion = int(año_pred)
            
            if año_prediccion <= max(años):
                print(f" Advertencia: El año {año_prediccion} ya tiene datos historicos")
                continuar = input("¿Desea continuar? (s/n): ").lower()
                if continuar != "s":
                    continue
            break
        
        except ValueError:
            print(" Por favor ingrese un año valido (numero entero) ")
            continue
        
    # Hacer prediccion
    estudiantes_predichos = mejor_a * año_prediccion + mejor_b
    
    print(f"\n" + "="*50 + "\n")
    print(f" RESULTADO DE LA PREDICCIÓN ")
    print(f"\n" + "="*50 + "\n")
    print(f" Año solicitado: {año_prediccion} ")
    print(f" Estudiantes estimados: {estudiantes_predichos:.0f} ")
    print(f" Ecuación: y = {mejor_a}x + {mejor_b} ")
    print(f" Error del modelo (MAE): {mejor_mae:.2f} estudiantes ")
    
    # Calcular precisión porcentual
    precision = (1 - mejor_mae / np.mean(estudiantes_hist)) * 100
    print(f" Precisión estimada: {precision:.1f}% ")
    
    # Preparar y mostrar gráfica
    print(f" \n Generando gráfica de regresión lineal... \n ")
    
    data_historica = [[años[i], estudiantes_hist[i]] for i in range(len(años))]
    años_extendidos = list(range(min(años), año_prediccion + 1))
    regresion_extendida = calcular_regrecion_lineal(años_extendidos, mejor_a, mejor_b)
    
    # Generar gráfica con función del plots.py
    plot_data(data_historica, regresion_extendida, años_extendidos)

    print(f" Análisis completado exitosamente! ")


def mostrar_informacion():
    
    """
    Muestra información sobre el programa
    """
    
    print(" \n INFORMACIÓN DEL PROGRAMA: \n ")
    print("  • Desarrollado para el Lab 7 de Informática I")
    print("  • Implementa algoritmos de ordenamiento y regresión lineal")
    print("  • Requiere archivos: notas_estudiantes.csv y hist_matriculados.csv")
    print("  • Librerías necesarias: numpy, matplotlib")
    print("  • Genera gráficos automáticamente en opciones 4, 5 y 6")
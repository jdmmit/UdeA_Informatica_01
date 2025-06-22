"""
MAIN.PY - Lab 7 Estadísticas Estudiantes 
Contiene todas las funciones para el procesamiento de datos
Autor: Juan David Murillo & Juan Camilo Medina
Curso: Informática I - Universidad de Antioquia

INSTRUCCIONES PARA EJECUTAR:
1. Asegúrate de tener los archivos: notas_estudiantes.csv y hist_matriculados.csv
2. Asegúrate de tener el archivo: funciones.py en la misma carpeta
3. Instala las librerías necesarias: pip install numpy matplotlib
4. Ejecuta: python main.py

NUEVAS CARACTERÍSTICAS:
- Gráficos automáticos en opciones 4, 5 y 6
- Visualización profesional de datos
- Interfaz mejorada con indicadores visuales
"""

# Importar todas las funciones del módulo funciones
from funciones import *


def mostrar_menu():

    """Muestra el menú principal del programa"""

    print("\n" + "="*65 + "\n")
    print(" ========== SISTEMA DE ESTADÍSTICAS ESTUDIANTES ========== ")
    print(" ========== Universidad de Antioquia - Lab 7 ========== ")
    print("\n" + "="*65 + "\n")
    print("1. Cargar datos desde archivo")
    print("2. Eliminar estudiante")
    print("3. Mayor nota de estudiante")
    print("4. Ordenar promedios + GRÁFICO (Algoritmo Burbuja)")
    print("5. Ordenar por cursos + GRÁFICO (Algoritmo Selección)")
    print("6. Predecir estudiantes + GRÁFICO (Regresión Lineal)")
    print("7. Salir del programa")
    print("\n" + "="*65 + "\n")


def main():

    """Función principal que ejecuta el programa"""

    print("Iniciando Sistema de Estadísticas Estudiantes...")
    mostrar_informacion()


    # Cargar datos automaticamente

    print("\n Cargar datos automaticamente... \n")

    while True:
        mostrar_menu()

        try:
            opcion: input("Seleccione una opción (1-7): ").strip()
            
            if opcion == "1":
                print("\n" + "="*65 + "\n")
                print("CARGAR DATOS DESDE ARCHIVO")
                print("\n" + "="*65 + "\n")
                cargar_datos()

            elif opciones == "2":
                print("\n" + "="*65 + "\n")
                print("ELIMINAR ESTUDIANTE")
                print("\n" + "="*65 + "\n")        
                eliminar_estudiantes()

            elif opcion == "3":
                print("\n" + "="*65 + "\n")
                print("MAYOR NOTA DE ESTUDIANTE")
                print("\n" + "="*65 + "\n")
                mayor_nota_estudiante()

            elif opcion == "4":
                print("\n" + "="*65 + "\n")
                print(" ORDENAR POR PROMEDIOS + GRAFICO (Algoritmo Burbuja)")
                print("\n" + "="*65 + "\n")
                ordenar_promedios_burbuja()

            elif opcion == "5":
                print("\n" + "="*65 + "\n")
                print("ORDENAR POR CURSOS + GRAFICO (Algoritmo Seleccion)")
                print("\n" + "="*65 + "\n")
                ordenar_cantidad_cursos_seleccion()

            elif opcion == "6":
                predecir_estudiantes()

            elif opcion == '0':
                print("\n" + "="*65 + "\n")
                print("¡Gracias por usar el Sistema de Estadísticas!")
                print("Desarrollado para Informática I")
                print("Universidad de Antioquia")
                print("\n" + "="*65 + "\n")
                break    
            
            else:
                print("Opción inválida. Por favor seleccione una opción del 0 al 6.")

        except KeyboardInterrupt:
            print("\n\n Programa interrumpido por el usuario. \n\n")
            print("¡Gracias por usar el sistema!")
            break

        except Exception as e:
            print(f"Error inesperado: {e}")
            print("El programa continuará funcionando... ")
            print("Tip: Asegúrate de tener instalado matplotlib")

        input("\n Presione Enter para continuar... \n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n Error crítico: {e} \n")
        print("Por favor, verifique que los archivos estén presentes:")
        print("notas_estudiantes.csv")
        print("hist_matriculados.csv") 
        print("funciones.py")
        print("Librerías: numpy, matplotlib")
        input("Presione Enter para salir...")
"""
Sistema de Monitoreo de Clima
Laboratorio 5 - Informática I
Autor: Estudiante
"""

import json
import csv
from datetime import datetime, timedelta
from utilidades import *

def main():
    """Función principal del programa"""
    print("=== SISTEMA DE MONITOREO DE CLIMA ===")
    print("Cargando datos del sistema...")

    # Cargar datos al iniciar
    usuarios = cargar_usuarios()
    variables = cargar_variables()
    registros = cargar_registros()
    estaciones = cargar_estaciones()

    print("Datos cargados exitosamente!")

    # Iniciar menú principal
    menu_principal(usuarios, variables, registros, estaciones)

def menu_principal(usuarios, variables, registros, estaciones):
    """Menú principal del sistema"""
    while True:
        print("\n" + "="*50)
        print("           MENÚ PRINCIPAL")
        print("="*50)
        print("1. Usuario registrado")
        print("2. Usuario visitante")
        print("3. Salir del sistema")
        print("="*50)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            usuario = autenticar_usuario(usuarios)
            if usuario:
                print(f"\n¡Bienvenido {usuario['nombre']}!")
                if usuario['rol'] == 'Administrador':
                    menu_administrador(usuarios, variables, registros, estaciones, usuario)
                elif usuario['rol'] == 'Operador':
                    menu_operador(usuarios, variables, registros, estaciones, usuario)
            else:
                print("\n❌ Credenciales incorrectas. Intente nuevamente.")

        elif opcion == '2':
            menu_visitante(variables, registros, estaciones)

        elif opcion == '3':
            # Guardar datos antes de salir
            guardar_usuarios(usuarios)
            guardar_registros(registros)
            guardar_estaciones(estaciones)
            print("\n¡Gracias por usar el sistema! Datos guardados exitosamente.")
            break

        else:
            print("\n❌ Opción no válida. Intente nuevamente.")

def autenticar_usuario(usuarios):
    """Autentica un usuario en el sistema"""
    print("\n--- AUTENTICACIÓN DE USUARIO ---")
    documento = input("Documento: ").strip()
    clave = input("Contraseña: ").strip()

    for usuario in usuarios:
        if usuario['codigo'] == documento and usuario['clave'] == clave:
            return usuario
    return None

def menu_administrador(usuarios, variables, registros, estaciones, usuario_actual):
    """Menú para usuarios administradores"""
    while True:
        print("\n" + "="*50)
        print("         MENÚ ADMINISTRADOR")
        print("="*50)
        print("1. Gestionar estaciones")
        print("2. Gestionar usuarios")
        print("3. Depuración de registros")
        print("4. Volver al menú inicial")
        print("="*50)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            gestionar_estaciones(estaciones, registros)
        elif opcion == '2':
            gestionar_usuarios(usuarios, usuario_actual)
        elif opcion == '3':
            depurar_registros(registros)
        elif opcion == '4':
            break
        else:
            print("\n❌ Opción no válida.")

def menu_operador(usuarios, variables, registros, estaciones, usuario_actual):
    """Menú para usuarios operadores"""
    while True:
        print("\n" + "="*50)
        print("          MENÚ OPERADOR")
        print("="*50)
        print("1. Seleccionar estación")
        print("2. Volver al menú inicial")
        print("="*50)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            seleccionar_estacion(variables, registros, estaciones)
        elif opcion == '2':
            break
        else:
            print("\n❌ Opción no válida.")

def menu_visitante(variables, registros, estaciones):
    """Menú para usuarios visitantes"""
    while True:
        print("\n" + "="*50)
        print("          MENÚ VISITANTE")
        print("="*50)
        print("1. Visualizar estadísticas")
        print("2. Volver al menú inicial")
        print("="*50)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            visualizar_estadisticas(variables, registros, estaciones)
        elif opcion == '2':
            break
        else:
            print("\n❌ Opción no válida.")

def gestionar_estaciones(estaciones, registros):
    """Gestión de estaciones"""
    while True:
        print("\n--- GESTIÓN DE ESTACIONES ---")
        print("1. Crear estación")
        print("2. Editar estación")
        print("3. Eliminar estación")
        print("4. Listar estaciones")
        print("5. Volver")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            crear_estacion(estaciones)
        elif opcion == '2':
            editar_estacion(estaciones)
        elif opcion == '3':
            eliminar_estacion(estaciones, registros)
        elif opcion == '4':
            listar_estaciones(estaciones)
        elif opcion == '5':
            break
        else:
            print("\n❌ Opción no válida.")

def gestionar_usuarios(usuarios, usuario_actual):
    """Gestión de usuarios"""
    while True:
        print("\n--- GESTIÓN DE USUARIOS ---")
        print("1. Crear usuario")
        print("2. Editar usuario")
        print("3. Eliminar usuario")
        print("4. Listar usuarios")
        print("5. Volver")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            crear_usuario(usuarios)
        elif opcion == '2':
            editar_usuario(usuarios)
        elif opcion == '3':
            eliminar_usuario(usuarios, usuario_actual)
        elif opcion == '4':
            listar_usuarios(usuarios)
        elif opcion == '5':
            break
        else:
            print("\n❌ Opción no válida.")

def seleccionar_estacion(variables, registros, estaciones):
    """Selección de estación para operaciones"""
    if not estaciones:
        print("\n❌ No hay estaciones registradas.")
        return

    print("\n--- ESTACIONES DISPONIBLES ---")
    for i, estacion in enumerate(estaciones, 1):
        print(f"{i}. {estacion['codigo']} - {estacion['nombre']}")

    try:
        opcion = int(input("\nSeleccione una estación: ")) - 1
        if 0 <= opcion < len(estaciones):
            estacion_seleccionada = estaciones[opcion]
            menu_estacion(variables, registros, estacion_seleccionada)
        else:
            print("\n❌ Opción no válida.")
    except ValueError:
        print("\n❌ Debe ingresar un número.")

def menu_estacion(variables, registros, estacion):
    """Menú de operaciones en una estación"""
    while True:
        print(f"\n--- ESTACIÓN: {estacion['nombre']} ---")
        print("1. Mostrar medidas")
        print("2. Ingresar medidas")
        print("3. Volver")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            mostrar_medidas_estacion(registros, estacion)
        elif opcion == '2':
            ingresar_medidas(variables, registros, estacion)
        elif opcion == '3':
            break
        else:
            print("\n❌ Opción no válida.")

def visualizar_estadisticas(variables, registros, estaciones):
    """Visualización de estadísticas para visitantes"""
    print("\n--- VISUALIZAR ESTADÍSTICAS ---")

    # Seleccionar período
    periodo = seleccionar_periodo()
    if not periodo:
        return

    # Seleccionar variables
    vars_seleccionadas = seleccionar_variables(variables)
    if not vars_seleccionadas:
        return

    # Seleccionar modo de visualización
    modo = seleccionar_modo_visualizacion()

    # Calcular y mostrar estadísticas
    calcular_estadisticas(registros, estaciones, vars_seleccionadas, periodo, modo)

if __name__ == "__main__":
    main()

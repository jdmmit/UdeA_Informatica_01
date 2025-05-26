import module_manageDB as db

def mostrar_menu():
    print("\n===== SISTEMA DE GESTIÓN DE ESTUDIANTES =====")
    print("1. Agregar estudiante")
    print("2. Consultar información")
    print("3. Calcular promedio de notas")
    print("4. Salir")
    return input("Seleccione una opción (1-4): ")

def main():
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            db.add_student()
        elif opcion == '2':
            db.show_information()
        elif opcion == '3':
            db.average_performance()
        elif opcion == '4':
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción inválida. Por favor intente de nuevo.")

if __name__ == '__main__':
    main()
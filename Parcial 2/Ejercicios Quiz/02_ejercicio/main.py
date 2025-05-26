import student_module

def main():
    while True:
        print("\n--- MENÚ GESTIÓN DE ESTUDIANTES ---")
        print("1. Agregar estudiante")
        print("2. Consultar información")
        print("3. Calcular promedio de notas")
        print("4. Salir")

        option = input("\nSelecciona una opción (1-4): ")

        if option == "1":
            student_module.add_student()
        elif option == "2":
            student_module.show_information()
        elif option == "3":
            student_module.Average_Performance()
        elif option == "4":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
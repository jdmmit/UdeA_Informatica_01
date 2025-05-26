import task_module

def main():
    
    print("\n====¡Bienvenido al Gestor de Tareas!\n====")

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar tarea")
        print("2. Ver tarea")
        print("3. Contar tareas pendientes")
        print("4. Salir")

        try:
            opcion = input("\nElige una opción (1-4): ")

            if opcion == "1":
                task_module.add_task()
            elif opcion == "2":
                task_module.view_task()
            elif opcion == "3":
                task_module.count_task_pen()
            elif opcion == "4":
                print("\n====¡Gracias por usar el Gestor de Tareas! ¡Hasta pronto!====")
                break
            else:
                print("\n====¡Error! Opción inválida. Por favor, elige una opción del 1 al 4.====")
        except Exception as e:
            print(f"\n====¡Ups! Ocurrió un error: {e}====")
            print("====Por favor, intenta de nuevo.====")

if __name__ == "__main__":
    main()
def load_tasks():
    
    try:
        with open("database_tasks.txt", "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        with open("database_tasks.txt", "w") as file:
            pass
        return []

def save_tasks(tasks):
    
    with open("database_tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    tasks = load_tasks()
    task_id = input("Ingrese el identificador de la tarea (por ejemplo: Task_3): ")

    
    if task_id.endswith('.txt'):
        task_id = task_id[:-4]

    if task_id in tasks:
        print("¡Error! La tarea ya está registrada.")
        return

    description = input("Ingrese una breve descripción (máx 20 caracteres): ")
    if len(description) > 20:
        description = description[:20]
        print("La descripción se ha recortado a 20 caracteres.")

    responsible = input("Ingrese el nombre del responsable: ")

    while True:
        status = input("Ingrese el estado (PEN para pendiente, LISTO para terminada): ").upper()
        if status in ["PEN", "LISTO"]:
            break
        print("Estado inválido. Use PEN o LISTO.")

    tasks.append(task_id)
    save_tasks(tasks)

    
    with open(task_id + ".txt", "w") as file:
        file.write(f"ID: {task_id}\n")
        file.write(f"Descripción: {description}\n")
        file.write(f"Responsable: {responsible}\n")
        file.write(f"Estado: {status}\n")

    print(f"¡Tarea {task_id} registrada correctamente!")

def view_task():
    task_id = input("Ingrese el identificador de la tarea que desea ver: ")
    if task_id.endswith('.txt'):
        task_id = task_id[:-4]

    tasks = load_tasks()
    if task_id not in tasks:
        print(f"¡Error! La tarea {task_id} no existe.")
        return

    try:
        with open(task_id + ".txt", "r") as file:
            task_details = file.read()
            print("\n--- Detalles de la tarea ---")
            print(task_details)
    except FileNotFoundError:
        print(f"¡Error! El archivo {task_id}.txt no se encuentra.")
        tasks.remove(task_id)
        save_tasks(tasks)
        print(f"Se ha eliminado {task_id} de la lista de tareas.")

def count_task_pen():
    tasks = load_tasks()
    pending_count = 0

    for task_id in tasks:
        try:
            with open(task_id + ".txt", "r") as file:
                for line in file:
                    if "Estado: PEN" in line:
                        pending_count += 1
                        break
        except FileNotFoundError:
            print(f"Advertencia: El archivo {task_id}.txt no se encuentra.")
            tasks.remove(task_id)
            save_tasks(tasks)

    print(f"Hay {pending_count} tareas pendientes.")
    return pending_count
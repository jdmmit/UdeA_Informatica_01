def add_student():
    # Pedimos los datos del estudiante
    id_student = input("Ingresa la cédula del estudiante: ")

    # Verificamos si ya existe
    with open("database_student.txt", "a+") as database:
        database.seek(0)  # Vamos al inicio del archivo para leer
        ids = database.read().splitlines()

        if id_student in ids:
            print("¡Este estudiante ya está registrado!")
            return

        # Si no existe, pedimos el resto de datos
        name = input("Nombre del estudiante: ")
        career = input("Carrera del estudiante: ")
        grade = input("Nota del curso: ")

        # Guardamos el ID en la base de datos principal
        database.write(id_student + "\n")

        # Creamos archivo individual del estudiante
        with open(f"{id_student}.txt", "w") as student_file:
            student_file.write(f"Nombre: {name}\n")
            student_file.write(f"Carrera: {career}\n")
            student_file.write(f"Nota: {grade}\n")

        print(f"Estudiante {name} registrado con éxito.")

def show_information():
    id_student = input("Ingresa la cédula del estudiante a consultar: ")

    try:
        with open(f"{id_student}.txt", "r") as student_file:
            info = student_file.read()
            print("\n--- INFORMACIÓN DEL ESTUDIANTE ---")
            print(info)
    except FileNotFoundError:
        print("Estudiante no encontrado.")

def Average_Performance():
    try:
        with open("database_student.txt", "r") as database:
            ids = database.read().splitlines()

        if not ids:
            print("No hay estudiantes registrados.")
            return

        total_grades = 0
        count = 0

        for id_student in ids:
            try:
                with open(f"{id_student}.txt", "r") as student_file:
                    lines = student_file.readlines()
                    for line in lines:
                        if line.startswith("Nota:"):
                            grade = float(line.split(":")[1].strip())
                            total_grades += grade
                            count += 1
            except:
                continue

        if count > 0:
            average = total_grades / count
            print(f"El promedio de notas es: {average:.2f}")
        else:
            print("No se encontraron notas para calcular.")
    except FileNotFoundError:
        print("No hay estudiantes registrados.")
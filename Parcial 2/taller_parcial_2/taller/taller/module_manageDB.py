def check_estudiante(doc):
    """Verifica si un estudiante ya está registrado"""
    try:
        with open('database_student.txt', 'r') as file:
            for line in file:
                if line.strip() == doc:
                    return True
        return False
    except FileNotFoundError:
        # Si el archivo no existe, crearlo
        with open('database_student.txt', 'w') as file:
            pass
        return False

def add_student():
    """Registra un nuevo estudiante"""
    doc = input('Ingrese el documento del estudiante: ')

    if check_estudiante(doc):
        print('Estudiante ya registrado')
    else:
        nombre = input('Ingrese el nombre del estudiante: ')
        carrera = input('Ingrese la carrera del estudiante: ')

        # Validación de la nota
        while True:
            try:
                nota = float(input('Ingrese la nota del estudiante: '))
                if 0 <= nota <= 5:  # Asumiendo escala de 0 a 5
                    break
                else:
                    print("La nota debe estar entre 0 y 5")
            except ValueError:
                print("Por favor ingrese un valor numérico")

        # Guardar información del estudiante
        with open(doc + '.txt', 'w') as file_estudiante:
            file_estudiante.write(f'Documento: {doc}\n')
            file_estudiante.write(f'Nombre: {nombre}\n')
            file_estudiante.write(f'Carrera: {carrera}\n')
            file_estudiante.write(f'Nota: {nota}\n')

        # Actualizar base de datos
        with open('database_student.txt', 'a') as file_DB:
            file_DB.write(doc + '\n')

        print(f"Estudiante {nombre} registrado exitosamente")

def show_information():
    """Muestra la información de un estudiante"""
    doc = input('Ingrese el documento del estudiante: ')

    if check_estudiante(doc):
        print('\n----Información del Estudiante----')
        try:
            with open(doc + '.txt', 'r') as file_estudiante:
                for line in file_estudiante:
                    print(line.strip())
        except FileNotFoundError:
            print(f"Error: Archivo del estudiante {doc} no encontrado")
    else:
        print('El estudiante no está registrado')

def average_performance():
    """Calcula el promedio de notas de todos los estudiantes"""
    try:
        with open('database_student.txt', 'r') as file_DB:
            suma = 0
            count = 0

            for doc in file_DB:
                doc = doc.strip()
                try:
                    with open(doc + '.txt', 'r') as file_estudiante:
                        for line in file_estudiante:
                            if line.startswith('Nota:'):
                                try:
                                    nota = float(line.split(':')[1].strip())
                                    suma += nota
                                    count += 1
                                except ValueError:
                                    print(f"Error: Nota inválida para estudiante {doc}")
                except FileNotFoundError:
                    print(f"Advertencia: Archivo del estudiante {doc} no encontrado")

            if count > 0:
                promedio = suma / count
                print(f'El promedio de las notas es: {promedio:.2f}')
            else:
                print('No hay estudiantes con notas registradas')
    except FileNotFoundError:
        print('No hay usuarios registrados')
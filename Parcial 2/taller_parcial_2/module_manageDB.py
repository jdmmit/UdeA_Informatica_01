def checkEstudiante(doc):
    file = open('database_student.txt', 'r')
    for line in file:
        if line[0:-1] == doc:
            return True
    return False

def add_student():
    doc = input('Ingrese el documento del estudiante: ')
    estudiante_reg = checkEstudiante(doc)
    if estudiante_reg == True:
        print('Estudiante ya registrado')
    else:
        nombre = input('Ingrese el nombre del estudiante: ')
        carrera = input('Ingrese la carrera del estudiante: ')
        nota = input('Ingrese la nota del estudiante: ')

        file_estudiante = open(doc + '.txt', 'w')
        file_estudiante.write('Documento: ' + doc + '\n')
        file_estudiante.write('Nombre: ' + nombre + '\n')
        file_estudiante.write('Carrera: ' + carrera + '\n')
        file_estudiante.write('Nota: ' + nota + '\n')
        file_estudiante.close()

        file_DB = open('database_student.txt', 'a')
        file_DB.write(doc + '\n')
        file_DB.close()

def show_information():
    
    doc = input('Ingrese el documento del estudiante: ')
    existEstudiante = checkEstudiante(doc)
    if existEstudiante:
        file_estudiante = open(doc + '.txt', 'r')
        for line in file_estudiante:
            print(line[0:-1])
        file_estudiante.close()

def average_performance():
    file_DB = open('database_student.txt', 'r')
    suma = 0
    i = 0
    for doc in file_DB:
        i += 1
        file_estudiante = open(doc[0:-1] + '.txt', 'r')
        for line_estudiante in file_estudiante:
            if 'Nota' in line_estudiante:
                nota = float(line_estudiante[6:])
                suma += nota
    if i == 0:
        print('No hay usuarios registrados')
    else:
        print('El promedio de las notas es: ', suma/i)

if __name__ == '__main__':
    add_student()


import module_manageDB as m_DB

Bandera = True
while(Bandera):
    print('Menu')
    print('-'*20)
    print('1. Agregar estudiante')
    print('2. Consultar información')
    print('3. Mostrar información del estudiante')
    print('4. Salir')
    print('-'*20)

    opcion = input('Ingrese una opción: ')

    if opcion == '1':
        m_DB.add_student()
    if opcion == '2':
        print("--------Informacion del estudiante--------")
        m_DB.show_information()
        print("-"*20)
    if opcion == '3':
        m_DB.average_performance()
    elif opcion == '4':
        Bandera = False
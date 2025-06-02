"""
Módulo de utilidades para el sistema de monitoreo de clima
Contiene funciones para manejo de datos, validaciones y operaciones básicas
"""

import json
import csv
from datetime import datetime, timedelta
import os

# ==================== FUNCIONES DE CARGA Y GUARDADO ====================

def cargar_usuarios():
    """Carga los usuarios desde el archivo CSV"""
    usuarios = []
    try:
        with open('usuarios.csv', 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                usuarios.append(fila)
    except FileNotFoundError:
        print("⚠️ Archivo usuarios.csv no encontrado. Se creará uno nuevo.")
        # Crear usuarios por defecto
        usuarios = [
            {'codigo': '1010101010', 'nombre': 'Mariana Montoya', 'clave': '1234', 'rol': 'Administrador'},
            {'codigo': '1111111111', 'nombre': 'Elkin Perez', 'clave': '1234', 'rol': 'Operador'},
            {'codigo': '1212121212', 'nombre': 'Camila Serna', 'clave': '1234', 'rol': 'Administrador'},
            {'codigo': '1313131313', 'nombre': 'Oscar Jaramillo', 'clave': '1234', 'rol': 'Operador'},
            {'codigo': '1234512345', 'nombre': 'Juan Perez', 'clave': '12345', 'rol': 'Administrador'}
        ]
        guardar_usuarios(usuarios)
    return usuarios

def guardar_usuarios(usuarios):
    """Guarda los usuarios en el archivo CSV"""
    with open('usuarios.csv', 'w', newline='', encoding='utf-8') as archivo:
        campos = ['codigo', 'nombre', 'clave', 'rol']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(usuarios)

def cargar_variables():
    """Carga las variables desde el archivo JSON"""
    try:
        with open('variables.json', 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("⚠️ Archivo variables.json no encontrado. Se creará uno nuevo.")
        variables = {
            "variables": {
                "temperatura": {"minimo": -10, "maximo": 50, "unidades": "°C"},
                "humedad": {"minimo": 0, "maximo": 100, "unidades": "%"},
                "presion": {"minimo": 800, "maximo": 1200, "unidades": "hPa"},
                "viento": {"minimo": 0, "maximo": 200, "unidades": "km/h"},
                "precipitacion": {"minimo": 0, "maximo": 500, "unidades": "mm"}
            }
        }
        with open('variables.json', 'w', encoding='utf-8') as archivo:
            json.dump(variables, archivo, indent=2, ensure_ascii=False)
        return variables

def cargar_registros():
    """Carga los registros desde el archivo JSON"""
    try:
        with open('registros.json', 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("⚠️ Archivo registros.json no encontrado. Se creará uno nuevo.")
        registros = {}
        guardar_registros(registros)
        return registros

def guardar_registros(registros):
    """Guarda los registros en el archivo JSON"""
    with open('registros.json', 'w', encoding='utf-8') as archivo:
        json.dump(registros, archivo, indent=2, ensure_ascii=False)

def cargar_estaciones():
    """Carga las estaciones desde el archivo CSV"""
    estaciones = []
    try:
        with open('estaciones.csv', 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                estaciones.append(fila)
    except FileNotFoundError:
        print("⚠️ Archivo estaciones.csv no encontrado. Se creará uno nuevo.")
        estaciones = [
            {'codigo': 'EST001', 'nombre': 'Estación Centro'},
            {'codigo': 'EST002', 'nombre': 'Estación Norte'},
            {'codigo': 'EST003', 'nombre': 'Estación Sur'}
        ]
        guardar_estaciones(estaciones)
    return estaciones

def guardar_estaciones(estaciones):
    """Guarda las estaciones en el archivo CSV"""
    with open('estaciones.csv', 'w', newline='', encoding='utf-8') as archivo:
        campos = ['codigo', 'nombre']
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(estaciones)

# ==================== FUNCIONES DE VALIDACIÓN ====================

def validar_documento(documento):
    """Valida que el documento tenga 10 dígitos numéricos"""
    return len(documento) == 10 and documento.isdigit()

def validar_nombre(nombre):
    """Valida que el nombre solo contenga letras y espacios"""
    return all(c.isalpha() or c.isspace() for c in nombre) and nombre.strip()

def validar_clave(clave):
    """Valida que la clave tenga mínimo 4 caracteres"""
    return len(clave) >= 4

def validar_fecha(fecha_str):
    """Valida que la fecha tenga formato YYYY-MM-DD y sea válida"""
    try:
        datetime.strptime(fecha_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validar_valor_variable(valor, variable_config):
    """Valida que un valor esté en el rango de la variable"""
    if valor == 'ND' or valor == -999:
        return True
    try:
        valor_num = float(valor)
        return variable_config['minimo'] <= valor_num <= variable_config['maximo']
    except ValueError:
        return False

# ==================== FUNCIONES DE GESTIÓN DE USUARIOS ====================

def crear_usuario(usuarios):
    """Crea un nuevo usuario"""
    print("\n--- CREAR NUEVO USUARIO ---")

    # Validar documento
    while True:
        documento = input("Documento (10 dígitos): ").strip()
        if not validar_documento(documento):
            print("❌ El documento debe tener exactamente 10 dígitos numéricos.")
            continue

        # Verificar que no exista
        if any(u['codigo'] == documento for u in usuarios):
            print("❌ Ya existe un usuario con ese documento.")
            continue
        break

    # Validar nombre
    while True:
        nombre = input("Nombre completo: ").strip()
        if not validar_nombre(nombre):
            print("❌ El nombre solo puede contener letras y espacios.")
            continue
        break

    # Validar clave
    while True:
        clave = input("Contraseña (mínimo 4 caracteres): ").strip()
        if not validar_clave(clave):
            print("❌ La contraseña debe tener mínimo 4 caracteres.")
            continue

        clave_confirm = input("Confirmar contraseña: ").strip()
        if clave != clave_confirm:
            print("❌ Las contraseñas no coinciden.")
            continue
        break

    # Seleccionar rol
    while True:
        print("\nRoles disponibles:")
        print("1. Administrador")
        print("2. Operador")
        opcion_rol = input("Seleccione el rol: ").strip()

        if opcion_rol == '1':
            rol = 'Administrador'
            break
        elif opcion_rol == '2':
            rol = 'Operador'
            break
        else:
            print("❌ Opción no válida.")

    # Crear usuario
    nuevo_usuario = {
        'codigo': documento,
        'nombre': nombre,
        'clave': clave,
        'rol': rol
    }

    usuarios.append(nuevo_usuario)
    print(f"\n✅ Usuario {nombre} creado exitosamente.")

def editar_usuario(usuarios):
    """Edita un usuario existente"""
    if not usuarios:
        print("\n❌ No hay usuarios registrados.")
        return

    print("\n--- EDITAR USUARIO ---")
    listar_usuarios(usuarios)

    try:
        indice = int(input("\nSeleccione el número del usuario a editar: ")) - 1
        if 0 <= indice < len(usuarios):
            usuario = usuarios[indice]

            print(f"\nEditando usuario: {usuario['nombre']}")

            # Editar nombre
            nuevo_nombre = input(f"Nuevo nombre (actual: {usuario['nombre']}): ").strip()
            if nuevo_nombre and validar_nombre(nuevo_nombre):
                usuario['nombre'] = nuevo_nombre

            # Editar clave
            nueva_clave = input(f"Nueva contraseña (actual: {usuario['clave']}): ").strip()
            if nueva_clave and validar_clave(nueva_clave):
                clave_confirm = input("Confirmar nueva contraseña: ").strip()
                if nueva_clave == clave_confirm:
                    usuario['clave'] = nueva_clave
                else:
                    print("❌ Las contraseñas no coinciden. No se cambió la contraseña.")

            # Editar rol
            print(f"\nRol actual: {usuario['rol']}")
            print("1. Administrador")
            print("2. Operador")
            opcion_rol = input("Nuevo rol (Enter para mantener actual): ").strip()

            if opcion_rol == '1':
                usuario['rol'] = 'Administrador'
            elif opcion_rol == '2':
                usuario['rol'] = 'Operador'

            print("\n✅ Usuario editado exitosamente.")
        else:
            print("\n❌ Número de usuario no válido.")
    except ValueError:
        print("\n❌ Debe ingresar un número.")

def eliminar_usuario(usuarios, usuario_actual):
    """Elimina un usuario"""
    if not usuarios:
        print("\n❌ No hay usuarios registrados.")
        return

    print("\n--- ELIMINAR USUARIO ---")
    listar_usuarios(usuarios)

    try:
        indice = int(input("\nSeleccione el número del usuario a eliminar: ")) - 1
        if 0 <= indice < len(usuarios):
            usuario = usuarios[indice]

            # No puede eliminarse a sí mismo
            if usuario['codigo'] == usuario_actual['codigo']:
                print("\n❌ No puede eliminar su propio usuario.")
                return

            confirmacion = input(f"\n¿Está seguro de eliminar a {usuario['nombre']}? (s/n): ").strip().lower()
            if confirmacion == 's':
                usuarios.pop(indice)
                print("\n✅ Usuario eliminado exitosamente.")
            else:
                print("\n❌ Eliminación cancelada.")
        else:
            print("\n❌ Número de usuario no válido.")
    except ValueError:
        print("\n❌ Debe ingresar un número.")

def listar_usuarios(usuarios):
    """Lista todos los usuarios"""
    if not usuarios:
        print("\n❌ No hay usuarios registrados.")
        return

    print("\n--- LISTA DE USUARIOS ---")
    for i, usuario in enumerate(usuarios, 1):
        print(f"{i}. {usuario['codigo']} - {usuario['nombre']} ({usuario['rol']})")

# ==================== FUNCIONES DE GESTIÓN DE ESTACIONES ====================

def crear_estacion(estaciones):
    """Crea una nueva estación"""
    print("\n--- CREAR NUEVA ESTACIÓN ---")

    nombre = input("Nombre de la estación: ").strip()
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return

    # Generar código automático
    if estaciones:
        ultimo_numero = max(int(est['codigo'][3:]) for est in estaciones if est['codigo'].startswith('EST'))
        nuevo_numero = ultimo_numero + 1
    else:
        nuevo_numero = 1

    codigo = f"EST{nuevo_numero:03d}"

    nueva_estacion = {
        'codigo': codigo,
        'nombre': nombre
    }

    estaciones.append(nueva_estacion)
    print(f"\n✅ Estación {nombre} creada con código {codigo}.")

def editar_estacion(estaciones):
    """Edita una estación existente"""
    if not estaciones:
        print("\n❌ No hay estaciones registradas.")
        return

    print("\n--- EDITAR ESTACIÓN ---")
    listar_estaciones(estaciones)

    try:
        indice = int(input("\nSeleccione el número de la estación a editar: ")) - 1
        if 0 <= indice < len(estaciones):
            estacion = estaciones[indice]

            nuevo_nombre = input(f"Nuevo nombre (actual: {estacion['nombre']}): ").strip()
            if nuevo_nombre:
                estacion['nombre'] = nuevo_nombre
                print("\n✅ Estación editada exitosamente.")
            else:
                print("\n❌ El nombre no puede estar vacío.")
        else:
            print("\n❌ Número de estación no válido.")
    except ValueError:
        print("\n❌ Debe ingresar un número.")

def eliminar_estacion(estaciones, registros):
    """Elimina una estación si no tiene registros"""
    if not estaciones:
        print("\n❌ No hay estaciones registradas.")
        return

    print("\n--- ELIMINAR ESTACIÓN ---")
    listar_estaciones(estaciones)

    try:
        indice = int(input("\nSeleccione el número de la estación a eliminar: ")) - 1
        if 0 <= indice < len(estaciones):
            estacion = estaciones[indice]

            # Verificar si tiene registros
            if estacion['codigo'] in registros and registros[estacion['codigo']]:
                print("\n❌ No se puede eliminar la estación porque tiene registros asociados.")
                return

            confirmacion = input(f"\n¿Está seguro de eliminar {estacion['nombre']}? (s/n): ").strip().lower()
            if confirmacion == 's':
                estaciones.pop(indice)
                print("\n✅ Estación eliminada exitosamente.")
            else:
                print("\n❌ Eliminación cancelada.")
        else:
            print("\n❌ Número de estación no válido.")
    except ValueError:
        print("\n❌ Debe ingresar un número.")

def listar_estaciones(estaciones):
    """Lista todas las estaciones"""
    if not estaciones:
        print("\n❌ No hay estaciones registradas.")
        return

    print("\n--- LISTA DE ESTACIONES ---")
    for i, estacion in enumerate(estaciones, 1):
        print(f"{i}. {estacion['codigo']} - {estacion['nombre']}")

# ==================== FUNCIONES DE MEDICIONES ====================

def mostrar_medidas_estacion(registros, estacion):
    """Muestra las medidas de una estación"""
    codigo_estacion = estacion['codigo']

    if codigo_estacion not in registros or not registros[codigo_estacion]:
        print(f"\n❌ No hay medidas registradas para {estacion['nombre']}.")
        return

    print(f"\n--- MEDIDAS DE {estacion['nombre']} ---")

    datos_estacion = registros[codigo_estacion]

    # Obtener todas las fechas
    fechas = set()
    for variable in datos_estacion:
        fechas.update(datos_estacion[variable].keys())

    fechas = sorted(fechas, reverse=True)

    if not fechas:
        print("❌ No hay medidas registradas.")
        return

    # Mostrar últimas 10 fechas
    print("\nÚltimas mediciones:")
    for fecha in fechas[:10]:
        print(f"\nFecha: {fecha}")
        for variable in datos_estacion:
            if fecha in datos_estacion[variable]:
                valores = datos_estacion[variable][fecha]
                valores_str = [str(v) if v != -999 else 'ND' for v in valores]
                print(f"  {variable}: {', '.join(valores_str)}")

def ingresar_medidas(variables, registros, estacion):
    """Ingresa nuevas medidas para una estación"""
    print(f"\n--- INGRESAR MEDIDAS PARA {estacion['nombre']} ---")

    # Obtener fecha actual
    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    print(f"Fecha: {fecha_actual}")

    codigo_estacion = estacion['codigo']

    # Inicializar estructura si no existe
    if codigo_estacion not in registros:
        registros[codigo_estacion] = {}

    vars_config = variables['variables']

    for variable, config in vars_config.items():
        print(f"\n{variable} ({config['unidades']}) - Rango: {config['minimo']} a {config['maximo']}")

        while True:
            valor_str = input(f"Valor para {variable} (o 'ND' si no disponible): ").strip()

            if valor_str.upper() == 'ND':
                valor = -999
                break

            try:
                valor = float(valor_str)
                if validar_valor_variable(valor, config):
                    break
                else:
                    print(f"❌ El valor debe estar entre {config['minimo']} y {config['maximo']}.")
            except ValueError:
                print("❌ Debe ingresar un número válido o 'ND'.")

        # Guardar el valor
        if variable not in registros[codigo_estacion]:
            registros[codigo_estacion][variable] = {}

        if fecha_actual not in registros[codigo_estacion][variable]:
            registros[codigo_estacion][variable][fecha_actual] = []

        registros[codigo_estacion][variable][fecha_actual].append(valor)

    print("\n✅ Medidas ingresadas exitosamente.")

# ==================== FUNCIONES DE ESTADÍSTICAS ====================

def seleccionar_periodo():
    """Permite seleccionar el período de tiempo para estadísticas"""
    print("\n--- SELECCIONAR PERÍODO ---")
    print("1. Últimos 7 días")
    print("2. Últimos 30 días")
    print("3. Elegir fechas manualmente")

    opcion = input("Seleccione una opción: ").strip()

    fecha_fin = datetime.now()

    if opcion == '1':
        fecha_inicio = fecha_fin - timedelta(days=7)
    elif opcion == '2':
        fecha_inicio = fecha_fin - timedelta(days=30)
    elif opcion == '3':
        while True:
            fecha_inicio_str = input("Fecha de inicio (YYYY-MM-DD): ").strip()
            if validar_fecha(fecha_inicio_str):
                fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d')
                break
            else:
                print("❌ Formato de fecha inválido.")

        while True:
            fecha_fin_str = input("Fecha de fin (YYYY-MM-DD): ").strip()
            if validar_fecha(fecha_fin_str):
                fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d')
                if fecha_fin >= fecha_inicio:
                    break
                else:
                    print("❌ La fecha de fin debe ser posterior a la de inicio.")
            else:
                print("❌ Formato de fecha inválido.")
    else:
        print("❌ Opción no válida.")
        return None

    return (fecha_inicio, fecha_fin)

def seleccionar_variables(variables):
    """Permite seleccionar las variables a analizar"""
    vars_config = variables['variables']
    vars_lista = list(vars_config.keys())

    print("\n--- SELECCIONAR VARIABLES ---")
    for i, variable in enumerate(vars_lista, 1):
        print(f"{i}. {variable}")
    print(f"{len(vars_lista) + 1}. Todas las variables")

    seleccion = input("\nSeleccione variables (números separados por comas): ").strip()

    try:
        if seleccion == str(len(vars_lista) + 1):
            return vars_lista

        indices = [int(x.strip()) - 1 for x in seleccion.split(',')]
        variables_seleccionadas = [vars_lista[i] for i in indices if 0 <= i < len(vars_lista)]

        if variables_seleccionadas:
            return variables_seleccionadas
        else:
            print("❌ No se seleccionaron variables válidas.")
            return None
    except ValueError:
        print("❌ Formato de selección inválido.")
        return None

def seleccionar_modo_visualizacion():
    """Permite seleccionar el modo de visualización"""
    print("\n--- MODO DE VISUALIZACIÓN ---")
    print("1. Visualizar por pantalla")
    print("2. Guardar en archivo Estadisticas.txt")

    while True:
        opcion = input("Seleccione una opción: ").strip()
        if opcion in ['1', '2']:
            return int(opcion)
        else:
            print("❌ Opción no válida.")

def calcular_estadisticas(registros, estaciones, variables_seleccionadas, periodo, modo):
    """Calcula y muestra las estadísticas"""
    fecha_inicio, fecha_fin = periodo

    resultados = []

    for variable in variables_seleccionadas:
        valores = []
        detalles_valores = []

        # Recopilar todos los valores de la variable en el período
        for codigo_estacion, datos_estacion in registros.items():
            if variable in datos_estacion:
                for fecha_str, valores_fecha in datos_estacion[variable].items():
                    fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
                    if fecha_inicio <= fecha <= fecha_fin:
                        for valor in valores_fecha:
                            if valor != -999:  # Excluir valores ND
                                valores.append(valor)
                                # Buscar nombre de estación
                                nombre_estacion = next((est['nombre'] for est in estaciones if est['codigo'] == codigo_estacion), codigo_estacion)
                                detalles_valores.append((valor, nombre_estacion, fecha_str))

        if valores:
            maximo = max(valores)
            minimo = min(valores)
            promedio = sum(valores) / len(valores)

            # Encontrar detalles del máximo y mínimo
            detalle_max = next(det for det in detalles_valores if det[0] == maximo)
            detalle_min = next(det for det in detalles_valores if det[0] == minimo)

            resultado = f"""
VARIABLE: {variable.upper()}
{'='*50}
Máximo: {maximo} - Estación: {detalle_max[1]} - Fecha: {detalle_max[2]}
Mínimo: {minimo} - Estación: {detalle_min[1]} - Fecha: {detalle_min[2]}
Promedio: {promedio:.2f}
Número de mediciones: {len(valores)}
"""
            resultados.append(resultado)
        else:
            resultado = f"""
VARIABLE: {variable.upper()}
{'='*50}
No hay datos disponibles para el período seleccionado.
"""
            resultados.append(resultado)

    # Mostrar o guardar resultados
    contenido_completo = f"""
ESTADÍSTICAS DEL SISTEMA DE MONITOREO
Período: {fecha_inicio.strftime('%Y-%m-%d')} a {fecha_fin.strftime('%Y-%m-%d')}
Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*70}
""" + "\n".join(resultados)

    if modo == 1:
        print(contenido_completo)
    else:
        with open('Estadisticas.txt', 'w', encoding='utf-8') as archivo:
            archivo.write(contenido_completo)
        print("\n✅ Estadísticas guardadas en Estadisticas.txt")

def depurar_registros(registros):
    """Función para depuración de registros (funcionalidad adicional)"""
    print("\n--- DEPURACIÓN DE REGISTROS ---")
    print("Esta funcionalidad compararía archivos duplicados.")
    print("Por ahora, se muestra un resumen de los registros actuales:")

    total_estaciones = len(registros)
    total_mediciones = 0

    for codigo_estacion, datos_estacion in registros.items():
        for variable, fechas in datos_estacion.items():
            for fecha, valores in fechas.items():
                total_mediciones += len(valores)

    print(f"\nTotal de estaciones con registros: {total_estaciones}")
    print(f"Total de mediciones: {total_mediciones}")

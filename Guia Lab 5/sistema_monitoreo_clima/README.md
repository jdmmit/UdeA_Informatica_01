# Sistema de Monitoreo de Clima

## Descripción
Este es un sistema de monitoreo de clima desarrollado en Python para el Laboratorio 5 de Informática I. 
Permite gestionar usuarios, estaciones de monitoreo, variables ambientales y registros de mediciones.

## Características
- **Gestión de usuarios**: Administradores y Operadores con diferentes permisos
- **Gestión de estaciones**: Crear, editar y eliminar estaciones de monitoreo
- **Registro de mediciones**: Ingresar y visualizar datos de variables ambientales
- **Estadísticas**: Calcular máximo, mínimo y promedio de variables en períodos específicos
- **Validaciones**: Validación completa de datos de entrada
- **Persistencia**: Datos guardados en archivos CSV y JSON

## Estructura del Proyecto
```
sistema_monitoreo_clima/
├── main.py              # Programa principal
├── utilidades.py        # Funciones auxiliares
├── usuarios.csv         # Base de datos de usuarios
├── variables.json       # Configuración de variables
├── registros.json       # Registros de mediciones
├── estaciones.csv       # Base de datos de estaciones
└── README.md           # Este archivo
```

## Cómo ejecutar
1. Asegúrate de tener Python 3.6 o superior instalado
2. Ejecuta el programa principal:
   ```bash
   python main.py
   ```

## Usuarios de prueba
- **Administrador**: 
  - Documento: 1010101010, Clave: 1234
  - Documento: 1212121212, Clave: 1234
- **Operador**: 
  - Documento: 1111111111, Clave: 1234
  - Documento: 1313131313, Clave: 1234

## Variables monitoreadas
- **Temperatura**: -10°C a 50°C
- **Humedad**: 0% a 100%
- **Presión**: 800 hPa a 1200 hPa
- **Viento**: 0 km/h a 200 km/h
- **Precipitación**: 0 mm a 500 mm

## Funcionalidades por rol

### Administrador
- Gestionar usuarios (crear, editar, eliminar)
- Gestionar estaciones (crear, editar, eliminar)
- Depuración de registros

### Operador
- Ingresar mediciones en estaciones
- Visualizar mediciones existentes

### Visitante
- Visualizar estadísticas de mediciones
- Exportar estadísticas a archivo

## Validaciones implementadas
- Documento: 10 dígitos numéricos
- Nombre: Solo letras y espacios
- Contraseña: Mínimo 4 caracteres
- Fechas: Formato YYYY-MM-DD válido
- Valores de variables: Dentro del rango permitido

## Notas técnicas
- Los valores "No Disponibles" se representan como -999 internamente
- Las fechas se manejan en formato ISO (YYYY-MM-DD)
- Los archivos se guardan automáticamente al salir del programa
- Se crean archivos de ejemplo si no existen al iniciar

## Autor
Desarrollado como parte del Laboratorio 5 de Informática I

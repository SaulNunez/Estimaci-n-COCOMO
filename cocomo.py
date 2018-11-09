from enum import Enum

class Cocomo():
    class Tipos(Enum):
        ORGANICO = 1
        SEMI_ACOPLADO = 2
        EMPOTRADO = 3

    class Modelo(Enum):
        BASICO = 1
        INTERMEDIO = 2
        AVANZADO = 3


    const_organico = {
        'a':2.40,
        'b':1.05,
        'c':2.50,
        'd':0.38
    }

    const_semi_organico = {
        'a':3.00,
        'b':1.12,
        'c':2.50,
        'd':0.35
    }

    const_empotrado = {
        'a':3.60,
        'b':1.20,
        'c':2.50,
        'd':0.33
    }

    indice_loc = {
        'Ensamblador': 320,
        'Macroensamblador': 213,
        'C': 150,
        'Fortran': 106,
        'Cobol': 106,
        'Pascal': 91,
        'Cobol ANSI 85': 91,
        'Basic': 91,
        'RPG': 80,
        'PL/I': 80,
        'Ada': 71,
        'Basic ANSI/Quick/Turbo': 64,
        'Java': 53,
        'Visual C++': 34,
        'Foxpro 2,5': 34,
        'Visual Basic': 32,
        'Delphi': 29,
        'C++': 29,
        'Visual Cobol': 20,
        'Clipper': 19,
        'Power Builder': 16,
        'Hoja de Calculo': 6
    }

    preguntas_grado_total_influencia = [
        '1) ¿Requiere el sistema copias de seguridad y de recuperación fiables?',
        '2) ¿Se requiere de comunicación de datos?',
        '3) ¿Existen funciones de procesamiento distribuido?',
        '4) ¿Es crítico el rendimiento?',
        '5) ¿Se ejecutará el sistema en un entorno operativo existente y fuertemente utilizado?',
        '6) ¿Requiere el sistema entrada de datos interactiva?',
        '7) ¿Requiere la entrada de datos interactiva que las transacciones de entrada se lleven a cao sobre múltiples pantallas u operaciones?',
        '8) ¿Se actualizan los archivos maestros de forma interactiva?',
        '9) ¿Son complejas las entradas, salidas, archivos o las peticiones?',
        '10) ¿Es complejo el procesamiento interno?',
        '11) ¿Se ha diseñado el código para ser reutilizable?',
        '12) ¿Estan incluidas en el diseño la conversión y la instalación?',
        '13) ¿Se ha diseñado el sistema para soportar múltiples instalaciones en diferentes organizaciones?',
        '14) ¿Se ha diseñado la aplicación para facilitar los cambios y para ser fácilmente utilizada por el usuario?'
    ]

    variables_fae = {
        'Flexibilidad requerida del software': {
            'Muy Bajo':0.75,
            'Bajo':0.88,
            'Nominal':1.00,
            'Alto':1.15,
            'Muy Alto':1.40
        },
        'Tamaño de la base de datos': {
            'Bajo':0.94,
            'Nominal':1.00,
            'Alto':1.08,
            'Muy Alto':1.16
        },
        'Complejidad del producto': {
            'Muy Bajo':0.70,
            'Bajo':0.85,
            'Nominal':1.00,
            'Alto':1.15,
            'Muy Alto':1.30,
            'Extremandamente Alto':1.65
        },
        'Restricciones del teimpo de ejecución':{
            'Nominal':1.00,
            'Alto':1.11,
            'Muy Alto':1.30,
            'Extremandamente Alto':1.66
        },
        'Restricciones del almacenamiento principal': {
            'Nominal':1.00,
            'Alto':1.06,
            'Muy Alto':1.21,
            'Extremandamente Alto':1.56
        },
        'Volatilidad de la máquina virtual':{
            'Bajo':0.87,
            'Nominal':1.00,
            'Alto':1.15,
            'Muy Alto':1.30
        },
        'Tiempo de respuesta del ordenador':{
            'Bajo':0.87,
            'Nominal':1.00,
            'Alto':1.07,
            'Muy Alto':1.15
        },
        'Capacidad del analista':{
            'Muy Bajo':1.46,
            'Bajo':1.19,
            'Nominal':1.00,
            'Alto':0.86,
            'Muy Alto':0.71
        },
        'Experiencia de la aplicación':{
            'Muy Bajo':1.29,
            'Bajo':1.13,
            'Nominal':1.00,
            'Alto':0.91,
            'Muy Alto':0.82
        },
        'Capacidad de los programadores':{
            'Muy Bajo':1.42,
            'Bajo':1.17,
            'Nominal':1.00,
            'Alto':0.86,
            'Muy Alto':0.70
        },
        'Experiencia en S.O utlizado':{
            'Muy Bajo':1.21,
            'Bajo':1.10,
            'Nominal':1.00,
            'Alto':0.90
        },
        'Experiencia en el lenguaje de programación':{
            'Muy Bajo':1.14,
            'Bajo':1.07,
            'Nominal':1.00,
            'Alto':0.95
        },
        'Prácticas de programación modernas':{
            'Muy Bajo':1.24,
            'Bajo':1.10,
            'Nominal':1.00,
            'Alto':0.91,
            'Muy Alto':0.82
        },
        'Utilización de herramientas':{
            'Muy Bajo':1.24,
            'Bajo':1.10,
            'Nominal':1.00,
            'Alto':0.91,
            'Muy Alto':0.83
        },
        'Limitaciones de planificacin del proyecto':{
            'Muy Bajo':1.23,
            'Bajo':1.08,
            'Nominal':1.00,
            'Alto':1.04,
            'Muy Alto':1.10
        }
    }
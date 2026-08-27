# Prompts Utilizados para Crear el Compilador

## Prompt Principal

```
Haga un compilador en Python que compile programas en C++

Requisitos:
1. Debe de subir los prompts utilizados
2. Debe de subir en pdf los archivos creados
3. Debe de subir el manual de cómo usar el compilador
4. Debe de subir imágenes del paso a paso desde la ejecución hasta la compilación del programa
```

## Prompts de Desarrollo

### 1. Compilador Principal (compiler.py)
```
Crea una clase CppCompiler en Python que:
- Compile archivos de C++ usando g++, clang++ o msvc
- Permita configurar niveles de optimización (-O0, -O1, -O2, -O3)
- Registre las compilaciones en un log JSON
- Ejecute programas compilados y capture su salida
- Maneje errores y advertencias del compilador
- Proporcione información del sistema
```

### 2. Interfaz Gráfica (gui.py)
```
Crea una interfaz gráfica con tkinter que:
- Permita seleccionar archivos C++ para compilar
- Muestre la salida de compilación en tiempo real
- Tenga botones para compilar, ejecutar y compilar+ejecutar
- Permita cambiar el compilador y nivel de optimización
- Muestre reportes de compilación
- Use colores para errores (rojo), advertencias (amarillo) y éxito (verde)
```

### 3. Ejemplos de Programas
```
Crea 5 programas de ejemplo en C++:
1. Hola Mundo - Programa básico
2. Calculadora - Operaciones matemáticas básicas
3. Ordenamiento - Uso de vectores y algoritmos STL
4. Clases - POO y sistemas de registro
5. Funciones Matemáticas - Recursión y funciones avanzadas
```

## Prompts Técnicos Específicos

### Compilación Multi-plataforma
```
Implementa soporte para:
- Windows (MSVC, MinGW)
- Linux (GCC, Clang)
- macOS (Clang)
Con detección automática del sistema operativo
```

### Manejo de Errores
```
Implementa:
- Captura de excepciones de compilación
- Timeout para procesos largos
- Validación de archivos de entrada
- Mensajes de error descriptivos
- Logging detallado de operaciones
```

### Características Avanzadas
```
Incluye:
- Compilación paralela (opcional)
- Depuración con flags -g y -gdb
- Análisis de advertencias
- Generación de ejecutables optimizados
- Estadísticas de compilación
```

## Prompts para Documentación

### Manual de Usuario
```
Crea un manual completo que incluya:
- Instalación y requisitos
- Guía de uso CLI y GUI
- Descripción de ejemplos
- Solución de problemas
- FAQ
```

### Archivos PDF
```
Genera PDFs con:
- Guía rápida de inicio
- Documentación del API
- Galería de ejemplos compilados
- Especificaciones técnicas
```

## Notas de Implementación

- **Lenguaje**: Python 3.7+
- **Librerías principales**: subprocess, json, pathlib, tkinter
- **Compiladores soportados**: g++, clang++, msvc
- **Sistemas operativos**: Windows, Linux, macOS
- **Interfaz**: CLI y GUI (tkinter)

## Ejemplo de Uso en Código

```python
from compiler import CppCompiler

# Crear instancia
compiler = CppCompiler(compiler_cmd="g++", optimization="-O2")

# Compilar
success, msg = compiler.compile("example.cpp", "output")

# Ejecutar
if success:
    compiler.run("output")
```

---

**Generado**: 2026-08-27
**Versión**: 1.0
**Autor**: Sistema Compilador C++ Python

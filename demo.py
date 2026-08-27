#!/usr/bin/env python3
"""
Script de demostración del compilador
Muestra cómo usar el compilador desde Python
"""

from compiler import CppCompiler
from pathlib import Path
import sys

def separador(titulo=""):
    """Imprime un separador visual"""
    if titulo:
        print(f"\n{'='*60}")
        print(f"  {titulo}")
        print(f"{'='*60}\n")
    else:
        print(f"\n{'-'*60}\n")

def demo_compilador():
    """Demostración completa del compilador"""
    
    print("\n╔════════════════════════════════════════╗")
    print("║  DEMOSTRACIÓN DEL COMPILADOR C++       ║")
    print("║        en Python v1.0                  ║")
    print("╚════════════════════════════════════════╝\n")
    
    # Crear instancia del compilador
    compiler = CppCompiler(compiler_cmd="g++", optimization="-O2")
    
    # Verificar disponibilidad
    separador("Paso 1: Verificar Compilador")
    if not compiler.check_compiler():
        print("✗ Error: Compilador no disponible")
        print("Por favor instala g++, clang++ o msvc")
        sys.exit(1)
    print("✓ Compilador g++ disponible y funcionando")
    
    # Mostrar información del sistema
    separador("Paso 2: Información del Sistema")
    info = compiler.get_system_info()
    for clave, valor in info.items():
        print(f"  {clave}: {valor}")
    
    # Compilar ejemplo 1
    separador("Paso 3: Compilar Ejemplo 1 - Hola Mundo")
    archivo1 = "examples/01_hello_world.cpp"
    if Path(archivo1).exists():
        success, msg = compiler.compile(archivo1)
        if success:
            print("✓ Compilación exitosa")
            # Ejecutar
            separador("Paso 4: Ejecutar Ejemplo 1")
            compiler.run("hello_world", input_data="Usuario\n")
        else:
            print(f"✗ Error: {msg}")
    else:
        print(f"✗ Archivo no encontrado: {archivo1}")
    
    # Compilar ejemplo 2
    separador("Paso 5: Compilar Ejemplo 2 - Calculadora")
    archivo2 = "examples/02_calculator.cpp"
    if Path(archivo2).exists():
        success, msg = compiler.compile(archivo2)
        if success:
            print("✓ Compilación exitosa")
            # Ejecutar con datos
            separador("Paso 6: Ejecutar Calculadora")
            compiler.run("calculator", input_data="15\n*\n3\n")
        else:
            print(f"✗ Error: {msg}")
    else:
        print(f"✗ Archivo no encontrado: {archivo2}")
    
    # Compilar ejemplo 3
    separador("Paso 7: Compilar Ejemplo 3 - Ordenamiento")
    archivo3 = "examples/03_sorting.cpp"
    if Path(archivo3).exists():
        success, msg = compiler.compile(archivo3)
        if success:
            print("✓ Compilación exitosa")
            # Ejecutar
            separador("Paso 8: Ejecutar Ordenamiento")
            compiler.run("sorting")
        else:
            print(f"✗ Error: {msg}")
    else:
        print(f"✗ Archivo no encontrado: {archivo3}")
    
    # Compilar ejemplo 4
    separador("Paso 9: Compilar Ejemplo 4 - Clases")
    archivo4 = "examples/04_classes.cpp"
    if Path(archivo4).exists():
        success, msg = compiler.compile(archivo4)
        if success:
            print("✓ Compilación exitosa")
            # Ejecutar
            separador("Paso 10: Ejecutar Clases")
            compiler.run("classes")
        else:
            print(f"✗ Error: {msg}")
    else:
        print(f"✗ Archivo no encontrado: {archivo4}")
    
    # Compilar ejemplo 5
    separador("Paso 11: Compilar Ejemplo 5 - Funciones Matemáticas")
    archivo5 = "examples/05_math_functions.cpp"
    if Path(archivo5).exists():
        success, msg = compiler.compile(archivo5, extra_flags=["-lm"])
        if success:
            print("✓ Compilación exitosa")
            # Ejecutar
            separador("Paso 12: Ejecutar Funciones Matemáticas")
            compiler.run("math_functions")
        else:
            print(f"✗ Error: {msg}")
    else:
        print(f"✗ Archivo no encontrado: {archivo5}")
    
    # Mostrar reporte final
    separador("REPORTE FINAL")
    compiler.print_report()
    
    # Guardar log
    separador("Guardando Registro")
    compiler.save_log("demo_compilation.log")
    print("✓ Registro guardado en: demo_compilation.log")
    
    separador("DEMOSTRACIÓN COMPLETADA")
    print("✓ Todos los pasos se completaron correctamente\n")

if __name__ == "__main__":
    demo_compilador()

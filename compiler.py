#!/usr/bin/env python3
"""
Compilador de C++ desarrollado en Python
Permite compilar, ejecutar y depurar programas en C++
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime
import platform
from typing import Dict, Tuple, Optional

class CppCompiler:
    """Clase principal del compilador de C++ en Python"""
    
    def __init__(self, compiler_cmd: str = "g++", optimization: str = "-O2"):
        """
        Inicializa el compilador
        
        Args:
            compiler_cmd: Comando del compilador (g++, clang++, etc)
            optimization: Nivel de optimización (-O0, -O1, -O2, -O3)
        """
        self.compiler_cmd = compiler_cmd
        self.optimization = optimization
        self.output_dir = Path("./build")
        self.source_dir = Path("./src")
        self.compilation_log = []
        self.errors = []
        self.warnings = []
        
        # Crear directorios necesarios
        self.output_dir.mkdir(exist_ok=True)
        self.source_dir.mkdir(exist_ok=True)
        
    def check_compiler(self) -> bool:
        """Verifica si el compilador está instalado"""
        try:
            result = subprocess.run(
                [self.compiler_cmd, "--version"],
                capture_output=True,
                timeout=5
            )
            return result.returncode == 0
        except FileNotFoundError:
            self.errors.append(f"Error: {self.compiler_cmd} no está instalado")
            return False
        except Exception as e:
            self.errors.append(f"Error al verificar compilador: {str(e)}")
            return False
    
    def compile(self, source_file: str, output_file: Optional[str] = None,
                extra_flags: list = None) -> Tuple[bool, str]:
        """
        Compila un archivo de C++
        
        Args:
            source_file: Ruta del archivo fuente
            output_file: Nombre del ejecutable (opcional)
            extra_flags: Flags adicionales del compilador
            
        Returns:
            Tupla (éxito, mensaje)
        """
        source_path = Path(source_file)
        
        if not source_path.exists():
            error_msg = f"Error: Archivo {source_file} no encontrado"
            self.errors.append(error_msg)
            return False, error_msg
        
        # Determinar nombre del ejecutable
        if output_file is None:
            output_file = source_path.stem
        
        output_path = self.output_dir / output_file
        
        # Construir comando de compilación
        flags = extra_flags if extra_flags else []
        cmd = [
            self.compiler_cmd,
            str(source_path),
            "-o", str(output_path),
            self.optimization,
            "-Wall",
            "-Wextra",
            *flags
        ]
        
        # Registrar compilación
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "source": str(source_path),
            "output": str(output_path),
            "command": " ".join(cmd)
        }
        
        print(f"\n{'='*60}")
        print(f"Compilando: {source_file}")
        print(f"{'='*60}")
        print(f"Comando: {' '.join(cmd)}")
        print(f"{'='*60}\n")
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            log_entry["return_code"] = result.returncode
            log_entry["stdout"] = result.stdout
            log_entry["stderr"] = result.stderr
            
            if result.returncode == 0:
                success_msg = f"✓ Compilación exitosa: {output_path}"
                print(f"\n{success_msg}\n")
                self.compilation_log.append(log_entry)
                return True, success_msg
            else:
                error_msg = f"✗ Error de compilación:\n{result.stderr}"
                print(f"\n{error_msg}\n")
                self.errors.append(error_msg)
                self.compilation_log.append(log_entry)
                
                # Procesar advertencias y errores
                self._process_compiler_output(result.stderr)
                return False, error_msg
                
        except subprocess.TimeoutExpired:
            error_msg = "Error: Tiempo de compilación excedido"
            self.errors.append(error_msg)
            return False, error_msg
        except Exception as e:
            error_msg = f"Error durante la compilación: {str(e)}"
            self.errors.append(error_msg)
            return False, error_msg
    
    def run(self, executable_name: str, args: list = None, input_data: str = None) -> Tuple[bool, str]:
        """
        Ejecuta un programa compilado
        
        Args:
            executable_name: Nombre del ejecutable
            args: Argumentos para el programa
            input_data: Datos de entrada (stdin)
            
        Returns:
            Tupla (éxito, salida)
        """
        exe_path = self.output_dir / executable_name
        
        if not exe_path.exists():
            error_msg = f"Error: Ejecutable {executable_name} no encontrado"
            self.errors.append(error_msg)
            return False, error_msg
        
        cmd = [str(exe_path)]
        if args:
            cmd.extend(args)
        
        print(f"\n{'='*60}")
        print(f"Ejecutando: {executable_name}")
        print(f"{'='*60}\n")
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=10,
                input=input_data
            )
            
            output = result.stdout
            if result.returncode != 0:
                output += f"\n[Error código {result.returncode}]\n{result.stderr}"
            
            print(output)
            print(f"\n{'='*60}\n")
            return result.returncode == 0, output
            
        except subprocess.TimeoutExpired:
            error_msg = "Error: Tiempo de ejecución excedido"
            self.errors.append(error_msg)
            return False, error_msg
        except Exception as e:
            error_msg = f"Error durante la ejecución: {str(e)}"
            self.errors.append(error_msg)
            return False, error_msg
    
    def compile_and_run(self, source_file: str, args: list = None, input_data: str = None) -> bool:
        """Compila y ejecuta un programa en una sola operación"""
        success, msg = self.compile(source_file)
        if success:
            exe_name = Path(source_file).stem
            self.run(exe_name, args, input_data)
            return True
        return False
    
    def _process_compiler_output(self, output: str):
        """Procesa la salida del compilador para extraer errores y advertencias"""
        for line in output.split('\n'):
            if 'warning:' in line.lower():
                self.warnings.append(line)
            elif 'error:' in line.lower():
                self.errors.append(line)
    
    def save_log(self, filename: str = "compilation.log"):
        """Guarda el registro de compilación en un archivo"""
        log_path = Path(filename)
        with open(log_path, 'w') as f:
            json.dump(self.compilation_log, f, indent=2)
        print(f"Registro guardado en: {log_path}")
    
    def get_system_info(self) -> Dict:
        """Obtiene información del sistema"""
        return {
            "sistema": platform.system(),
            "arquitectura": platform.machine(),
            "python_version": platform.python_version(),
            "compilador": self.compiler_cmd,
            "timestamp": datetime.now().isoformat()
        }
    
    def print_report(self):
        """Imprime un reporte de la compilación"""
        print("\n" + "="*60)
        print("REPORTE DE COMPILACIÓN")
        print("="*60)
        print(f"Compilaciones realizadas: {len(self.compilation_log)}")
        print(f"Errores: {len(self.errors)}")
        print(f"Advertencias: {len(self.warnings)}")
        
        if self.errors:
            print("\nErrores:")
            for error in self.errors:
                print(f"  - {error}")
        
        if self.warnings:
            print("\nAdvertencias:")
            for warning in self.warnings:
                print(f"  - {warning}")
        
        print("\nInformación del sistema:")
        for key, value in self.get_system_info().items():
            print(f"  {key}: {value}")
        print("="*60 + "\n")


def main():
    """Función principal"""
    print("\n╔═══════════════════════════════════════╗")
    print("║  Compilador de C++ en Python v1.0    ║")
    print("╚═══════════════════════════════════════╝\n")
    
    # Crear instancia del compilador
    compiler = CppCompiler()
    
    # Verificar disponibilidad del compilador
    if not compiler.check_compiler():
        print("Error: No se puede usar el compilador")
        sys.exit(1)
    
    print(f"✓ Compilador {compiler.compiler_cmd} disponible\n")


if __name__ == "__main__":
    main()

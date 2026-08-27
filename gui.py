#!/usr/bin/env python3
"""
Interfaz Gráfica (GUI) para el Compilador de C++ en Python
Usa tkinter para proporcionar una interfaz visual amigable
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
from pathlib import Path
from compiler import CppCompiler
import threading
import json
from datetime import datetime


class CompilerGUI:
    """Interfaz gráfica del compilador"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Compilador C++ - Interfaz Gráfica")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        
        self.compiler = CppCompiler()
        self.current_file = None
        self.is_compiling = False
        
        self._setup_styles()
        self._create_widgets()
        self._check_compiler()
    
    def _setup_styles(self):
        """Configura los estilos de la interfaz"""
        self.root.configure(bg='#f0f0f0')
        
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar colores
        style.configure('TButton', font=('Helvetica', 10))
        style.configure('Header.TLabel', font=('Helvetica', 12, 'bold'))
        style.configure('TFrame', background='#f0f0f0')
    
    def _create_widgets(self):
        """Crea los widgets de la interfaz"""
        
        # Frame superior
        top_frame = ttk.Frame(self.root)
        top_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        
        title_label = ttk.Label(top_frame, text="╔════════════════════════════════╗\n║  Compilador de C++ en Python  ║\n╚═════════��══════════════════════╝", 
                               font=('Helvetica', 14, 'bold'), justify=tk.CENTER)
        title_label.pack()
        
        # Frame de controles
        control_frame = ttk.LabelFrame(self.root, text="Controles", padding=10)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Fila 1: Seleccionar archivo
        select_frame = ttk.Frame(control_frame)
        select_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(select_frame, text="Archivo fuente:").pack(side=tk.LEFT, padx=5)
        self.file_label = ttk.Label(select_frame, text="Ninguno seleccionado", foreground="red")
        self.file_label.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        ttk.Button(select_frame, text="Seleccionar", command=self._select_file).pack(side=tk.RIGHT, padx=5)
        
        # Fila 2: Opciones
        options_frame = ttk.Frame(control_frame)
        options_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(options_frame, text="Optimización:").pack(side=tk.LEFT, padx=5)
        self.opt_var = tk.StringVar(value="-O2")
        opt_combo = ttk.Combobox(options_frame, textvariable=self.opt_var, 
                                 values=["-O0", "-O1", "-O2", "-O3"], state="readonly", width=10)
        opt_combo.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(options_frame, text="Compilador:").pack(side=tk.LEFT, padx=5)
        self.compiler_var = tk.StringVar(value="g++")
        compiler_combo = ttk.Combobox(options_frame, textvariable=self.compiler_var, 
                                      values=["g++", "clang++", "msvc"], state="readonly", width=10)
        compiler_combo.pack(side=tk.LEFT, padx=5)
        
        # Fila 3: Botones principales
        buttons_frame = ttk.Frame(control_frame)
        buttons_frame.pack(fill=tk.X, pady=10)
        
        self.compile_btn = ttk.Button(buttons_frame, text="Compilar", command=self._compile)
        self.compile_btn.pack(side=tk.LEFT, padx=5)
        
        self.run_btn = ttk.Button(buttons_frame, text="Ejecutar", command=self._run, state=tk.DISABLED)
        self.run_btn.pack(side=tk.LEFT, padx=5)
        
        self.compile_run_btn = ttk.Button(buttons_frame, text="Compilar y Ejecutar", command=self._compile_and_run)
        self.compile_run_btn.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(buttons_frame, text="Limpiar", command=self._clear_output).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(buttons_frame, text="Ver Reporte", command=self._show_report).pack(side=tk.RIGHT, padx=5)
        
        # Frame de salida
        output_frame = ttk.LabelFrame(self.root, text="Salida de Compilación", padding=10)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.output_text = scrolledtext.ScrolledText(output_frame, height=20, width=80, 
                                                      font=('Courier', 9), bg='#1e1e1e', fg='#00ff00')
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        # Configurar tags para colores
        self.output_text.tag_config("success", foreground="#00ff00")
        self.output_text.tag_config("error", foreground="#ff0000")
        self.output_text.tag_config("warning", foreground="#ffff00")
        self.output_text.tag_config("info", foreground="#00aaff")
        
        # Barra de estado
        self.status_var = tk.StringVar(value="Estado: Listo")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)
    
    def _log(self, message, tag="info"):
        """Agrega un mensaje al área de salida"""
        self.output_text.insert(tk.END, message + "\n", tag)
        self.output_text.see(tk.END)
        self.root.update()
    
    def _check_compiler(self):
        """Verifica disponibilidad del compilador"""
        if self.compiler.check_compiler():
            self._log("✓ Compilador disponible", "success")
        else:
            self._log("✗ Compilador no disponible", "error")
            messagebox.showerror("Error", "No se encontró compilador C++ instalado")
    
    def _select_file(self):
        """Abre diálogo para seleccionar archivo"""
        filename = filedialog.askopenfilename(
            title="Seleccionar archivo C++",
            filetypes=[("C++ files", "*.cpp *.cc *.cxx"), ("C files", "*.c"), ("All files", "*.*")]
        )
        if filename:
            self.current_file = filename
            self.file_label.config(text=filename, foreground="green")
            self._log(f"Archivo seleccionado: {filename}", "info")
    
    def _compile(self):
        """Compila el archivo seleccionado"""
        if not self.current_file:
            messagebox.showwarning("Advertencia", "Por favor selecciona un archivo")
            return
        
        self.is_compiling = True
        self.compile_btn.config(state=tk.DISABLED)
        self.status_var.set("Estado: Compilando...")
        
        def compile_thread():
            self.compiler.optimization = self.opt_var.get()
            self.compiler.compiler_cmd = self.compiler_var.get()
            
            self._log("\n" + "="*60, "info")
            self._log("INICIANDO COMPILACIÓN", "info")
            self._log("="*60, "info")
            
            success, msg = self.compiler.compile(self.current_file)
            
            if success:
                self._log(msg, "success")
                self.run_btn.config(state=tk.NORMAL)
            else:
                self._log(msg, "error")
            
            self.is_compiling = False
            self.compile_btn.config(state=tk.NORMAL)
            self.status_var.set("Estado: Listo")
        
        thread = threading.Thread(target=compile_thread, daemon=True)
        thread.start()
    
    def _run(self):
        """Ejecuta el programa compilado"""
        if not self.current_file:
            messagebox.showwarning("Advertencia", "Por favor compila primero")
            return
        
        exe_name = Path(self.current_file).stem
        self._log("\n" + "="*60, "info")
        self._log(f"EJECUTANDO: {exe_name}", "info")
        self._log("="*60, "info")
        
        success, output = self.compiler.run(exe_name)
        
        if success:
            self._log(output, "success")
        else:
            self._log(output, "error")
    
    def _compile_and_run(self):
        """Compila y ejecuta en una operación"""
        if not self.current_file:
            messagebox.showwarning("Advertencia", "Por favor selecciona un archivo")
            return
        
        self.is_compiling = True
        self.compile_btn.config(state=tk.DISABLED)
        self.status_var.set("Estado: Compilando y ejecutando...")
        
        def compile_run_thread():
            self.compiler.optimization = self.opt_var.get()
            self.compiler.compiler_cmd = self.compiler_var.get()
            
            self._log("\n" + "="*60, "info")
            self._log("COMPILANDO Y EJECUTANDO", "info")
            self._log("="*60, "info")
            
            if self.compiler.compile_and_run(self.current_file):
                self.run_btn.config(state=tk.NORMAL)
            
            self.is_compiling = False
            self.compile_btn.config(state=tk.NORMAL)
            self.status_var.set("Estado: Listo")
        
        thread = threading.Thread(target=compile_run_thread, daemon=True)
        thread.start()
    
    def _clear_output(self):
        """Limpia el área de salida"""
        self.output_text.delete(1.0, tk.END)
        self._log("Área de salida limpiada", "info")
    
    def _show_report(self):
        """Muestra un reporte de compilación"""
        report_window = tk.Toplevel(self.root)
        report_window.title("Reporte de Compilación")
        report_window.geometry("600x400")
        
        report_text = scrolledtext.ScrolledText(report_window, font=('Courier', 9))
        report_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Generar reporte
        report = "╔════════════════════════════════════════╗\n"
        report += "║     REPORTE DE COMPILACIÓN            ║\n"
        report += "╚════════════════════════════════════════╝\n\n"
        
        report += f"Compilaciones: {len(self.compiler.compilation_log)}\n"
        report += f"Errores: {len(self.compiler.errors)}\n"
        report += f"Advertencias: {len(self.compiler.warnings)}\n\n"
        
        if self.compiler.compilation_log:
            report += "═══ REGISTROS DE COMPILACIÓN ═══\n"
            for i, log in enumerate(self.compiler.compilation_log, 1):
                report += f"\n{i}. {log['source']}\n"
                report += f"   Salida: {log['output']}\n"
                report += f"   Hora: {log['timestamp']}\n"
                report += f"   Código retorno: {log['return_code']}\n"
        
        report_text.insert(1.0, report)
        report_text.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    gui = CompilerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

#include <iostream>
#include <cmath>

using namespace std;

// Función recursiva para factorial
long long factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

// Función para calcular números de Fibonacci
long long fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// Función para verificar si es primo
bool esPrimo(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    }
    return true;
}

int main() {
    cout << "╔════════════════════════════════════╗" << endl;
    cout << "║  Funciones Matemáticas            ║" << endl;
    cout << "╚════════════════════════════════════╝" << endl << endl;
    
    int numero = 10;
    
    cout << "Número seleccionado: " << numero << endl << endl;
    
    // Factorial
    cout << "Factorial de " << numero << ": " << factorial(numero) << endl;
    
    // Fibonacci
    cout << "Fibonacci de " << numero << ": " << fibonacci(numero) << endl;
    
    // Primo
    cout << "¿Es " << numero << " primo? " << (esPrimo(numero) ? "Sí" : "No") << endl;
    
    // Raíz cuadrada
    cout << "Raíz cuadrada de " << numero << ": " << sqrt(numero) << endl;
    
    // Potencia
    cout << numero << " elevado a 3: " << pow(numero, 3) << endl;
    
    return 0;
}

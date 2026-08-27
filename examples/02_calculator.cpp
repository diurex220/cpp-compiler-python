#include <iostream>
#include <cmath>

using namespace std;

int main() {
    cout << "╔════════════════════════════════════╗" << endl;
    cout << "║  Calculadora Básica                ║" << endl;
    cout << "╚════════════════════════════════════╝" << endl << endl;
    
    double num1, num2;
    char operador;
    
    cout << "Ingresa primer número: ";
    cin >> num1;
    
    cout << "Ingresa operador (+, -, *, /): ";
    cin >> operador;
    
    cout << "Ingresa segundo número: ";
    cin >> num2;
    
    double resultado;
    bool operacion_valida = true;
    
    switch(operador) {
        case '+':
            resultado = num1 + num2;
            break;
        case '-':
            resultado = num1 - num2;
            break;
        case '*':
            resultado = num1 * num2;
            break;
        case '/':
            if (num2 != 0) {
                resultado = num1 / num2;
            } else {
                cout << "Error: División por cero" << endl;
                operacion_valida = false;
            }
            break;
        default:
            cout << "Error: Operador inválido" << endl;
            operacion_valida = false;
    }
    
    if (operacion_valida) {
        cout << "\nResultado: " << num1 << " " << operador << " " << num2 << " = " << resultado << endl;
    }
    
    return 0;
}

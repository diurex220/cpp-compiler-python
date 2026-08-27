#include <iostream>
#include <string>
#include <cctype>

using namespace std;

class Persona {
public:
    string nombre;
    int edad;
    string ciudad;
    
    Persona(string n, int e, string c) : nombre(n), edad(e), ciudad(c) {}
    
    void mostrar() {
        cout << "Nombre: " << nombre << endl;
        cout << "Edad: " << edad << endl;
        cout << "Ciudad: " << ciudad << endl;
    }
};

int main() {
    cout << "╔════════════════════════════════════╗" << endl;
    cout << "║  Sistema de Registro de Personas   ║" << endl;
    cout << "╚════════════════════════════════════╝" << endl << endl;
    
    Persona p1("Juan García", 28, "Madrid");
    Persona p2("María López", 35, "Barcelona");
    Persona p3("Carlos Martínez", 42, "Valencia");
    
    Persona personas[] = {p1, p2, p3};
    
    cout << "═══════════════════════════════════\n";
    cout << "Personas registradas:\n";
    cout << "═══════════════════════════════════\n\n";
    
    for (int i = 0; i < 3; i++) {
        cout << "Persona " << (i + 1) << ":" << endl;
        personas[i].mostrar();
        cout << endl;
    }
    
    // Calcular edad promedio
    int suma_edades = 0;
    for (int i = 0; i < 3; i++) {
        suma_edades += personas[i].edad;
    }
    
    cout << "Edad promedio: " << (suma_edades / 3) << " años" << endl;
    
    return 0;
}

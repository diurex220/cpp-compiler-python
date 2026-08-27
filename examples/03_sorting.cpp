#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    cout << "╔════════════════════════════════════╗" << endl;
    cout << "║  Ordenamiento de Números           ║" << endl;
    cout << "╚════════════════════════════════════╝" << endl << endl;
    
    vector<int> numeros = {64, 34, 25, 12, 22, 11, 90, 45, 56, 78};
    
    cout << "Números originales: ";
    for (int num : numeros) {
        cout << num << " ";
    }
    cout << endl << endl;
    
    // Ordenar usando sort
    sort(numeros.begin(), numeros.end());
    
    cout << "Números ordenados (ascendente): ";
    for (int num : numeros) {
        cout << num << " ";
    }
    cout << endl;
    
    // Ordenar descendente
    sort(numeros.begin(), numeros.end(), greater<int>());
    
    cout << "Números ordenados (descendente): ";
    for (int num : numeros) {
        cout << num << " ";
    }
    cout << endl;
    
    // Estadísticas
    cout << "\nEstadísticas:" << endl;
    cout << "Cantidad: " << numeros.size() << endl;
    cout << "Máximo: " << *max_element(numeros.begin(), numeros.end()) << endl;
    cout << "Mínimo: " << *min_element(numeros.begin(), numeros.end()) << endl;
    
    return 0;
}

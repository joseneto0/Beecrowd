#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int contadorPositivas;
    double notas, soma;
    while (contadorPositivas != 2){
        cin >> notas;
        if (notas >= 0 && notas <= 10){
            soma += notas;
            contadorPositivas++;
        } else {
            cout << "nota invalida" << endl;
        }
    }
    double media = soma / 2;
    cout << fixed << setprecision(2);
    cout << "media = " << media << endl;
    return 0;
}
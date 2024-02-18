#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int contadorPositivas, continuar;
    double notas, soma;
    while (continuar != 2){
        cin >> notas;
        if (notas >= 0 && notas <= 10){
            soma += notas;
            contadorPositivas++;
        } else {
            cout << "nota invalida" << endl;
        } if (contadorPositivas == 2){
            cout << fixed << setprecision(2);
            cout << "media = " << soma / 2<< endl;
            cout << "novo calculo (1-sim 2-nao)" << endl;
            cin >> continuar;
            while (continuar < 1 || continuar > 2){
                cout << "novo calculo (1-sim 2-nao)" << endl;
                cin >> continuar;
            }
            if (continuar == 1){
                soma = 0;
                contadorPositivas = 0;
            }
        }
    }
    return 0;
}

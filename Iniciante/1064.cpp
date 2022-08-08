#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    float valores, soma = 0;
    int contador = 0;
    for (int i=0; i<6;i++){
        cin >> valores;
        if (valores > 0){
            contador += 1;
            soma += valores;
        }
    }
    cout << fixed << setprecision(1);
    cout << contador << " valores positivos" << endl;
    cout << soma / contador << endl;
    return 0;
}

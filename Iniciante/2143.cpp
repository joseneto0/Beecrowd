#include <iostream>

using namespace std;

int main(){
    int t, valor=0, soma=0;
    while (t != 0){
        cin >> t;
        for (int i = 0; i < t ; i++){
            cin >> valor;
            if ((valor-1) % 2 == 0){
                soma = (valor - 1) * 2 + 1;
            } else {
                soma = (valor - 2) * 2 + 2;
            }
            cout << soma << endl;
            soma = 0;
        }
    }
    return 0;
}

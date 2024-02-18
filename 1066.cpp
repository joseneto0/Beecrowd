#include <iostream>

using namespace std;

int main(){
    int valores;
    int lista[4] = {};
    for (int i=0; i<5;i++){
        cin >> valores;
        if (valores % 2 == 0){
            lista[0] += 1;
        }
        if (valores % 2 != 0){
            lista[1] += 1;
        }
        if (valores > 0){
            lista[2] += 1;
        }
        if (valores < 0){
            lista[3] += 1;
        }
    }
    cout << lista[0] << " valor(es) par(es)" << endl;
    cout << lista[1] << " valor(es) impar(es)" << endl;
    cout << lista[2] << " valor(es) positivo(s)" << endl;
    cout << lista[3] << " valor(es) negativo(s)" << endl;
    return 0;
}

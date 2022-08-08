#include <iostream>

using namespace std;

int main(){
    int valor, contador = 0;
    cin >> valor;
    for (int i=valor; contador != 6; i++){
        if (i % 2 != 0){
            cout << i << endl;
            contador += 1;
        }
    }
    return 0;
}

#include <iostream>

using namespace std;

int main(){
    int notas[6] = {100,50,20,10,5,2};
    int cont=0, a=0, b=0, conta=0;
    while (true){
        cin >> a >> b;
        if (a == 0 && b == 0){
            break;
        }
        conta = b - a;
        for (int i = 0; i<6; i++){
            if (conta / notas[i] == 1){
                conta -= notas[i];
                cont ++;
            }
        }
        if (cont == 2){
            cout << "possible" << endl;
        } else {
            cout << "impossible" << endl;
        }
        cont = 0;
    }
    return 0;
}

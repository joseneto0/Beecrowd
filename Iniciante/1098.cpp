#include <iostream>

using namespace std;

int main(){
    double i = 0, j = 1, contador = 0;
    for (i; i<=2; j){
        cout << "I=" << i << " J=" << j << endl;
        j += 1;
        contador ++;
        if (contador == 3){
            i += 0.2;
            j = 1 + i;
            contador = 0;
        }
    }
    return 0;
}

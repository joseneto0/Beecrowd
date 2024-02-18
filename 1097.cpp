#include <iostream>

using namespace std;

int main(){
    int i = 1, j = 7, contador = 0;
    for (i; i<=9; j-=1){
        cout << "I=" << i << " J=" << j << endl;
        contador += 1;
        if (contador == 3){
            i += 2;
            j += 5;
            contador = 0;
        }
    }
    return 0;
}

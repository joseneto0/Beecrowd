#include <iostream>

using namespace std;

int main(){
    int valores;
    int contador = 0;
    for (int i=0; i<5;i++){
        cin >> valores;
        if (valores % 2 == 0){
            contador += 1;
        }
    }
    cout << contador << " valores pares" << endl;
    return 0;
}

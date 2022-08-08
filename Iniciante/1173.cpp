#include <iostream>

using namespace std;

int main(){
    int N[10];
    int valor;
    cin >> valor;
    for (int i=0; i<10; i++){
        N[i] = valor;
        cout << "N[" << i << "] = " << N[i] << endl;
        valor *= 2;
    }
    return 0;
}
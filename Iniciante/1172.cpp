#include <iostream>

using namespace std;

int main(){
    int lista[10];
    for (int i=0; i<10; i++){
        cin >> lista[i];
        if (lista[i] <= 0){
            lista[i] = 1;
        }
        cout << "X[" << i << "] = " << lista[i] << endl;
    }
    return 0;
}

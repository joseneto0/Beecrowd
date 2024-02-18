#include <iostream>

using namespace std;

int main(){
    int valor, valores;
    cin >> valor;
    int lista[] = {0,0};
    for (int i=0; i<valor; i++){
        cin >> valores;
        if (valores >= 10 && valores <= 20){
            lista[0] += 1;
        } else {
            lista[1] += 1;
        }
    }
    cout << lista[0] << " in" << endl;
    cout << lista[1] << " out" << endl;
    return 0;
}

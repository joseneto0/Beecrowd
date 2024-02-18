#include <iostream>

using namespace std;

int main(){
    int x, y, soma = 0, aux;
    cin >> x >> y;
    if (y > x){
        aux = y;
        y = x;
        x = aux;
    }
    for (x; x>=y; x--){
        if (x % 13 != 0){
            soma += x;
        }
    }
    cout << soma << endl;
    return 0;
}

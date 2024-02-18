#include <iostream>

using namespace std;

int main(){
    int n, valores, s, aux=0;
    cin >> n;
    while (true){
        if (aux == n){
            break;
        }
        cin >> valores;
        for (int i=1; i<valores; i++){
            if (valores % i == 0){
                s += i;
            }
        }
        if (s == valores){
            cout << valores << " eh perfeito" << endl;
        } else {
            cout << valores << " nao eh perfeito" << endl;
        }
        aux += 1;
        s = 0;
    }
    return 0;
}

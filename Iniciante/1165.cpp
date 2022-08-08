#include <iostream>

using namespace std;

int main(){
    int n, valores=0, aux=0, qntdDivisoes=0;
    cin >> n;
    while (aux < n){
        cin >> valores;
        for (int i=1;i<=valores;i++){
            if (valores % i == 0){
                qntdDivisoes += 1;
            }
        }
        if (qntdDivisoes == 2){
            cout << valores << " eh primo" << endl;
        } else {
            cout << valores << " nao eh primo" << endl;
        }
        aux += 1;
        qntdDivisoes = 0;
    }
    return 0;
}

#include <bits/stdc++.h>

using namespace std;

int main(void){
    int n;
    cin >> n;
    vector<int> valores(n);
    for (int i = 0; i < n; i++){
        cin >> valores[i];
    }
    vector<int> zeros(n);
    for (int i = 0; i < n; i++){
        zeros[i] = 0;
    }
    int altura;
    int flechas = 0;
    int zero = 0;
    altura = valores[0];
    while (true){
        int ind = find(valores.begin(), valores.end(), altura) - valores.begin();
        for (int i = ind; i < n; i++){
            if (valores[i] == altura){
                altura--;
                valores[i] = 0;
            } if (altura == 0){
                flechas++;
                if (i == n - 1){
                    altura = valores[n-1];
                } else {
                    altura = valores[i+1];
                }
            } else {
                if (i == n-1){
                    flechas++;
                }
            }
        }
        for (int i = 0; i < n; i++){
            if (zeros[i] == valores[i]){
                zero++;
            } else {
                altura = valores[i];
                zero = 0;
                break;
            }
        }
        if (zero == n){
            break;
        }
    }
    cout << flechas << endl;
    return 0;
}
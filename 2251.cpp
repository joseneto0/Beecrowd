#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n, teste = 1;
    while (true){
        cin >> n;
        if (n == 0){
            break;
        }
        cout << "Teste " << teste << "\n";
        cout << (int)pow(2, n) - 1 << "\n";
        cout << "\n";
        teste++;
    }
    return 0;
}
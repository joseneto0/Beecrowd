#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int m,n;
    while (true){
        cin >> m >> n;
        if (m <= 0 || n <= 0){
            break;
        }
        int soma = 0;
        for (int i = min(m, n); i <= max(m, n); i++){
            cout << i << " ";
            soma += i;
        }
        cout << "Sum=" << soma << "\n";
    }
    return 0;
}
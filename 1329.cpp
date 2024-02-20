#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define all(x) x.begin(),x.end()


int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    while (true){
        int n;
        cin >> n;
        if (n == 0){
            break;
        }
        int maria = 0, joao = 0, aux;
        for (int i = 0; i < n; i++){
            cin >> aux;
            if (aux == 0) maria++;
            else joao++;
        }
        cout << "Mary won " << maria << " times and John won " << joao << " times" << "\n";
    }
    return 0;
}
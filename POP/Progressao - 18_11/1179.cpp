#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int x;
    vector<int> par, impar;
    for (int i = 0; i < 15; i++){
        cin >> x;
        if (par.size() == 5){
            for (int i = 0; i < 5; i++){
                cout << "par[" << i << "] = " << par[i] << "\n";
            }
            par.clear();
        }
        if (impar.size() == 5){
            for (int i = 0; i < 5; i++){
                cout << "impar[" << i << "] = " << impar[i] << "\n";
            }
            impar.clear();
        }
        if (x % 2 == 0){
            par.push_back(x);
        } else {
            impar.push_back(x);
        }
    }
    for (int i = 0; i < impar.size(); i++){
        cout << "impar[" << i << "] = " << impar[i] << "\n";
    }
    for (int i = 0; i < par.size(); i++){
        cout << "par[" << i << "] = " << par[i] << "\n";
    }
    return 0;
}
#include <bits/stdc++.h>

using namespace std;

int main(void){
    int n, v;
    cin >> n;
    vector<int> pares;
    vector<int> impares;
    for (int i = 0; i < n; i++){
        cin >> v;
        if (v % 2 == 0){
            pares.push_back(v);
        } else{
            impares.push_back(v);
        }
    }
    sort(pares.begin(), pares.end());
    sort(impares.begin(), impares.end(), greater<int>());
    for (int i = 0; i < pares.size(); i++){
        cout << pares[i] << '\n';
    }
    for (int i = 0; i < impares.size(); i++){
        cout << impares[i] << '\n';
    }
    return 0;
}
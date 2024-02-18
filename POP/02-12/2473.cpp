//torneio
#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int aux;
    set<int> dezenas;
    vector<string> possibiladades = {"sena", "quina", "quadra", "terno", "azar", "azar", "azar"};
    for (int i = 0; i < 6; i++){
        cin >> aux;
        dezenas.insert(aux);
    }
    for (int i = 0; i < 6; i++){
        cin >> aux;
        dezenas.erase(aux);
    }
    cout << possibiladades[dezenas.size()] << "\n";
    return 0;
}
#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> grafo;
vector<bool> visitados;

void dfs(int i){
    visitados[i] = true;
    for (auto x: grafo[i]){
        if (!visitados[x]){
            dfs(x);
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int m, n;
    cin >> m >> n;
    string s1, s2, s3;
    map<string, int> frequencia;
    grafo.assign(10000, vector<int>());
    visitados.assign(10000, false);
    for (int i = 1; i <= n; i++){
        cin >> s1 >> s2 >> s3;
        
    }
    int cont = 0;
    for (int i = 1; i <= 10000; i++){
        if (!visitados[i]){
            cont++;
            dfs(i);
        }
    }
    cout << cont << "\n";
    return 0;
}
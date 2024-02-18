#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> grafo;
vector<bool> visitados;
int cont = 0;
void dfs(int i){
    visitados[i] = true;
    for (auto x: grafo[i]){
        if (!visitados[x]){
            dfs(x);
            cont+=2;
        }
    }
}

void solve(){
    int n, v, a, x, y;
    cin >> n;
    cin >> v >> a;
    grafo.assign(v+1, vector<int>());
    visitados.assign(v+1, false);
    for (int i = 0; i < a; i++){
        cin >> x >> y;
        grafo[x].push_back(y);
        grafo[y].push_back(x);
    }
    dfs(n);
    cout << cont << "\n";
    cont = 0;
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int t;
    cin >> t;
    while (t--){
        solve();
    }
    return 0;
}
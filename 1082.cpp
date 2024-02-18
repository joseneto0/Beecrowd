#include <bits/stdc++.h>

using namespace std;


vector<vector<int>> grafo;
vector<bool> visitados;
string alfabeto = "abcdefghijklmnopqrstuvwxyz";
string s = "";
void dfs(int i){
    visitados[i] = true;
    s += alfabeto[i];
    for (auto x: grafo[i]){
        if (!visitados[x]){
            dfs(x);
        }
    }
}

int busca(char x){
    int inicio = 0, fim = alfabeto.size(), meio;
    while (inicio <= fim){
        meio = (inicio + fim) / 2;
        if (alfabeto[meio] == x){
            return meio;
        } else if (alfabeto[meio] < x){
            inicio = meio + 1;
        } else {
            fim = meio - 1;
        }
    }
}

void solve(int caso){   
    int v, e, bA, bB;
    cin >> v >> e;
    grafo.assign(alfabeto.size(), vector<int>());
    visitados.assign(alfabeto.size(), true);
    char a, b;
    for (int i = 0; i < e; i++){
        cin >> a >> b;
        bA = busca(a);
        bB = busca(b);
        grafo[bA].push_back(bB);
        grafo[bB].push_back(bA);
    }
    for (int i = 0; i < v; i++){
        visitados[i] = false;
    }
    cout << "Case #" << caso << ":\n";
    int cont = 0;
    for (int i = 0; i < alfabeto.size(); i++){
        if (!visitados[i]){
            dfs(i);
            sort(s.begin(), s.end());
            for (auto x: s){
                cout << x << ",";
            }
            cout << "\n";
            cont++;
            s = "";
        }
    }
    cout << cont << " connected components" << "\n";
}   

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int t;
    cin >> t;
    int caso = 1;
    while (t--){
        solve(caso);
        caso++;
        cout << "\n";
    }
    return 0;
}
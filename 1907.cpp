#include <bits/stdc++.h>

using namespace std;

vector<vector<char>> matriz;
int n, m;

void dfs(int i, int j){
    matriz[i][j] = 'o';
    if (i > 0 && matriz[i-1][j] == '.'){
        dfs(i-1, j);
    }
    if (i < n-1 && matriz[i+1][j] == '.'){
        dfs(i+1, j);
    }
    if (j > 0 && matriz[i][j-1] == '.'){
        dfs(i, j-1);
    }
    if (j < m-1 && matriz[i][j+1] == '.'){
        dfs(i, j+1);
    }
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    matriz.assign(n, vector<char>(m));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cin >> matriz[i][j];
        }
    }
    int cont = 0;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            if (matriz[i][j] == '.'){
                dfs(i, j);
                cont++;
            }
        }
    }
    cout << cont << "\n";
    return 0;
}
#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define all(x) x.begin(),x.end()

void solve(vector<vector<int>> &matriz){
    for (int i = 0; i < 9; i++){
        vector<int> freq(10, 0);
        for (int j = 0; j < 9; j++){
            freq[matriz[i][j]]++;
        }
        for (int j = 0; j < 9; j++){
            if (freq[matriz[i][j]] > 1){
                
                cout << "NAO" << "\n";
                return;
            }
        }
    }
    for (int i = 0; i < 9; i++){
        vector<int> freq(10, 0);
        for (int j = 0; j < 9; j++){
            freq[matriz[j][i]]++;
        }
        for (int j = 0; j < 9; j++){
            if (freq[matriz[j][i]] > 1){
                cout << "NAO" << "\n";
                return;
            }
        }
    }
    cout << "SIM" << "\n";
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n;
    cin >> n;
    for (int _ = 1; _ <= n; _++){
        vector<vector<int>> matriz(9, vector<int>(9));
        for (int i = 0; i < 9; i++){
            for (int j = 0; j < 9; j++){
                cin >> matriz[i][j];
            }
        }
        cout << "Instancia " << _ << "\n";
        solve(matriz);
        cout << "\n";
    }
    return 0;
}
#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define all(x) x.begin(),x.end()

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int h, p, f;
    while (true){
        cin >> h >> p >> f;
        if (!h && !p && !f){
            break;
        }
        vector<vector<int>> matriz(h, vector<int>(p));
        for (int i = 0; i < h; i++){
            for (int j = 0; j < p; j++){
                cin >> matriz[i][j];
            }
        }
        queue<int> a;
        int aux;
        for (int i = 0; i < f; i++){
            cin >> aux;
            a.push(aux);
        }
        bool end = false;
        for (int i = p-1; i >= 0; i--){
            if (end){
                break;
            }
            for (int j = h-1; j >= 0; j--){
                if (a.size() == 0){
                    end = true;
                    break;
                }
                if (matriz[j][i] == 0){
                    aux = a.front();
                    a.pop();
                    matriz[j][i] = aux;
                }
            }
        }
        for (int i = 0; i < h; i++){
            cout << matriz[i][0];
            for (int j = 1; j < p; j++){
                cout << " " << matriz[i][j];
            }
            cout << "\n";
        }
    }
    
    return 0;
}
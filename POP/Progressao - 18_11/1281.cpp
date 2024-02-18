#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int n, m, p, aux;
    string s;
    double valor;
    cin >> n;
    map<string, double> dicio;
    for (int i = 0; i < n; i++){
        cin >> m;
        for (int j = 0; j < m; j++){
            cin >> s >> valor;
            dicio[s] = valor;
        }
        cin >> p;
        double soma = 0;
        for (int j = 0; j < p; j++){
            cin >> s >> aux;
            soma += (dicio[s] * aux);
        }
        cout << fixed << "R$ " << setprecision(2) << soma << '\n';
        dicio.clear();
    }
    return 0;
}
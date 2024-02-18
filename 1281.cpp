#include <bits/stdc++.h>

using namespace std;

int main(void){
    int n;
    double valorFinal = 0;
    cin >> n;
    map<string, double> dict;
    while (n--){
        int m;
        cin >> m;
        for (int i=0; i<m; i++){
            string nome;
            double preco;
            cin >> nome >> preco;
            dict[nome] = preco;
        }
        int p;
        cin >> p;
        for (int j=0; j<p; j++){
            string fruta;
            int qntd;
            cin >> fruta >> qntd;
            if (dict.find(fruta) != dict.end()){
                valorFinal += (qntd * dict[fruta]);
            }
        }
        cout << setprecision(2) << fixed;
        cout << "R$ " << valorFinal << '\n';
        valorFinal = 0;
        dict.clear();
    }
}
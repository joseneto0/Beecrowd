#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define all(x) x.begin(),x.end()

bool cmp(pair<int, int> &x, pair<int, int> &y){
    return x.second < y.second;
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n, teste = 1;
    while (true){
        cin >> n;
        if (n == 0){
            break;
        }
        if (teste > 1) cout<<"\n";
        map<int, int> mp;
        int x, y;
        double soma = 0, qntd = 0;
        for (int i = 0; i < n; i++){
            cin >> x >> y;
            mp[y/x] += x;
            soma += y;
            qntd += x;
        }
        cout << "Cidade# " << teste << ":";
        cout << "\n";
        for (auto x: mp){
            cout << x.second << "-" << x.first << " ";
        }
        cout << "\n";
        double media = soma/qntd;
        stringstream aux;
        aux << media;
        string aux1 = "";
        if (fmod(soma, qntd) == 0){
            aux1 = aux.str() + ".00";
        } else {
            bool ponto = false;
            int cont = 0;
            for (int i = 0; i < aux.str().size(); i++){
                if (cont == 2){
                    break;
                }
                if (ponto){
                    cont++;
                }
                if (aux.str()[i] == '.'){
                    ponto = true;
                    aux1 += aux.str()[i];
                    continue;
                }
                aux1 += aux.str()[i];
            }
            if (cont < 2){
                for (int i = 0; i < 2 - cont; i++){
                    aux1 += '0';
                }
            }
        }
        cout << "Consumo medio: " <<  aux1 << " m3.";
        cout << "\n";
        teste++;
    }
    return 0;
}
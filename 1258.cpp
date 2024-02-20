#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define all(x) x.begin(),x.end()

struct camisa {
    string nome, cor, tamanho;
};

bool cmp(camisa &a, camisa &b){
    if (a.cor == b.cor){
        if (a.tamanho == b.tamanho){
            return a.nome < b.nome;
        }
        return a.tamanho > b.tamanho;
    }
    return a.cor < b.cor;
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n, cont = 0;
    while (true){
        cin >> n;
        cin.ignore();
        if (n == 0){
            break;
        }
        if (cont > 0){
            cout << "\n";
        }
        vector<camisa> a(n);
        for (int i = 0; i < n; i++){
            getline(cin, a[i].nome);
            cin >> a[i].cor >> a[i].tamanho;
            cin.ignore();
        }
        sort(all(a), cmp);
        for (auto i : a){
            cout << i.cor << " " << i.tamanho << " " << i.nome << "\n";
        }
        cont++;
    }    
    return 0;
}
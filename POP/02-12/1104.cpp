//lista
#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int a, b, aux;
    set<int> alice, beatriz, juncao;
    while(true){
        cin >> a >> b;
        if (a == 0 && b == 0){
            break;
        }
        for(int i = 0; i < a; i++){
            cin >> aux;
            alice.insert(aux);
        }
        for(int i = 0; i < b; i++){
            cin >> aux;
            beatriz.insert(aux);
        }
        set_union(alice.begin(), alice.end(), beatriz.begin(), beatriz.end(), inserter(juncao, juncao.end()));
        cout << min(juncao.size() - beatriz.size(), juncao.size() - alice.size()) << "\n";
        alice.clear();
        beatriz.clear();
        juncao.clear();
    }
    return 0;
}
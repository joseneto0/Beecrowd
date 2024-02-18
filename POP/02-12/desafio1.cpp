#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    string nome;
    set<string> alunos;
    for (int i = 0; i < n; i++){
        cin >> nome;
        alunos.insert(nome);
    }
    cout << alunos.size() << "\n";
    return 0;
}

#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    string nome;
    cin >> n;
    for (int i=0;i<n;i++){
        cin >> nome;
        cout << fixed << setprecision(2) << nome.size() * 0.01 << endl;
    }
    return 0;
}

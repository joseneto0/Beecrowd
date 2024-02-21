#include <bits/stdc++.h>

#define ll long long int
#define all(x) x.begin(), x.end()

using namespace std;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int n;
    cin >> n;
    cin.ignore();
    for (int i = 0; i < n; i++){
        string s, aux;
        stringstream x;
        set<string> a;
        getline(cin, s);
        x << s;
        while (x >> aux){
            a.insert(aux);
        }
        int cont = 0, t = a.size();
        for (auto b: a){
            if (cont == t-1) cout << b;
            else cout << b << " ";
            cont++;
        }
        cout << "\n";
    }
    return 0;
}
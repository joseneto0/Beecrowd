#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define all(x) x.begin(),x.end()

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n;
    cin >> n;
    vector<string> a;
    string s, aux;
    auto comp = [](string x, string y){
        return x.size() > y.size();
    };
    for (int i = 0; i <= n; i++){
        getline(cin, s);
        stringstream x(s);
        while (getline(x, aux, ' ')) {
            a.push_back(aux);
        }
        sort(all(a), comp);
        for (int i = 0; i < a.size(); i++){
            if (i == a.size() - 1) cout << a[i];
            else cout << a[i] << " ";
        }
        cout << "\n";
        a.clear();
    }
    return 0;
}
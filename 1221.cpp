#include <bits/stdc++.h>

#define ll long long int
#define all(x) x.begin(), x.end()

using namespace std;


void solve(){
    ll n;
    cin >> n;
    if (n == 0 || n == 1){
        cout << "Not Prime" << "\n";
        return;
    }
    if (n == 2){
        cout << "Prime" << "\n";
        return;
    }
    int cont = 0;
    for (int i = 2; i < sqrt(n)+1; i++){
        if (n % i == 0) cont++;
        if (cont == 2) break;
    }
    cout << (cont >= 1 ? "Not Prime" : "Prime") << "\n";
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int t;
    cin >> t;
    while (t--){
        solve();
    }
    return 0;
}
#include <bits/stdc++.h>

using namespace std;

int cont = 0;

int fibbo(int x){
    cont++;
    if (x <= 1) return x;
    return fibbo(x-1) + fibbo(x-2);
}

void solve(){
    int n;
    cin >> n;
    int res = fibbo(n);
    cont--;
    cout << "fib(" << n << ") = " << cont << " calls = " << res << "\n";
    cont = 0;
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int t;
    cin >> t;
    while (t--){
        solve();
    }
}
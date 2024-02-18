#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
vector<ll> memo;
ll fatorial(int x){
    if (memo[x] != -1){
        return memo[x];
    }
    if (x > 1){
        memo[x] = x * fatorial(x-1);
    } else {
        memo[x] = 1;
    }
    return memo[x];
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int m,n;
    while (cin >> m >> n){
        memo.assign(max(m, n)+1, -1);
        ll f = fatorial(max(m,n));
        cout << f + fatorial(min(m, n)) << "\n";
    }
    return 0;
}
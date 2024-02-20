#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define all(x) x.begin(),x.end()

ll josephus(ll n, ll k){
    if (n == 1){
        return 1;
    }
    return (josephus(n-1, k) + k - 1) % n + 1;
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++){
        ll n, k;
        cin >> n >> k;
        cout << "Case " << i << ": " << josephus(n, k) << "\n";
    }
    return 0;
}
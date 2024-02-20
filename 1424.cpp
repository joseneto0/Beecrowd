#include <bits/stdc++.h>

#define ll long long int

using namespace std;

signed main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    ll n, m, aux;
    map<ll, vector<ll>> mp;
    while (cin >> n >> m){
        for (ll i = 0; i < n; i++){
            cin >> aux;
            mp[aux].push_back(i+1);
        }
        ll k, v;
        for (ll i = 0; i < m; i++){
            cin >> k >> v;
            if (k > mp[v].size()){
                cout << 0 << "\n";
            } else {
                cout << mp[v][k-1] << "\n";
            }
        }
        mp.clear();
    }
    return 0;
}
#include <bits/stdc++.h>

#define int long long

using namespace std;

signed main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int n, m, aux;
    map<int, vector<int>> mp;
    while (cin >> n >> m){
        for (int i = 0; i < n; i++){
            cin >> aux;
            mp[aux].push_back(i+1);
        }
        int k, v;
        for (int i = 0; i < m; i++){
            cin >> k >> v;
            k--;
            if (mp[v][k] <= n) cout << mp[v][k] << "\n";
            else cout << 0 << "\n";
        }
        mp.clear();
    }
    return 0;
}
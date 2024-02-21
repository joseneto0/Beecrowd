#include <bits/stdc++.h>

#define ll long long int
#define all(x) x.begin(), x.end()

using namespace std;

vector<ll> id, sz;

ll find(ll x){
    return id[x] = (id[x] == x ? x : find(id[x]));
}

void unionn(ll x, ll y){
    x = find(x);
    y = find(y);
    if (sz[x] > sz[y]){
        swap(x, y);
    }
    id[x] = y;
    sz[y] += sz[x];
}


int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    ll r, c;
    cin >> r >> c;
    id = vector<ll>(r+1);
    sz = vector<ll>(r+1, 1);
    iota(all(id), 0);
    ll v, w, p;
    vector<tuple<ll, ll, ll>> grafo;
    for (ll i = 0; i < c; i++){
        cin >> v >> w >> p;
        grafo.emplace_back(p, v, w);
    }
    sort(all(grafo));
    ll ans = 0;
    for (auto i: grafo){
        tie(p, v, w) = i;
        if (find(v) != find(w)){
            unionn(v, w);
            ans += p;
        }
    }
    cout << ans << "\n";
    
    return 0;
}
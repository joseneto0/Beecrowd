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
    ll m, n;
    while (true){
        cin >> m >> n;
        if (m == 0 && n == 0){
            break;
        }
        id = vector<ll>(m+1);
        sz = vector<ll>(m+1, 1);
        iota(all(id), 0);
        ll x, y, z;
        ll soma = 0;
        vector<tuple<ll, ll, ll>> grafo;
        for (ll i = 0; i < n; i++){
            cin >> x >> y >> z;
            soma += z;
            grafo.emplace_back(z, x, y);
        }
        sort(all(grafo));
        ll c = 0;
        for (auto i: grafo){
            tie(z, x, y) = i;
            if (find(x) != find(y)){
                unionn(x, y);
                c += z;
            }
        }
        cout << soma - c << "\n";
    }
    return 0;
}
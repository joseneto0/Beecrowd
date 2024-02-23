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

ll kruskal(vector<tuple<ll, ll, ll>> &grafo, ll n){
    ll ans = 0;
    ll w, a, b;
    for (auto i: grafo){
        tie(w, a, b) = i;
        if (find(a) != find(b)){
            unionn(a, b);
            ans += w;
        }
    }
    return ans;
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    ll m, n;
    while (true){
        cin >> m >> n;
        if (m == 0 &&  n == 0){
            break;
        }
        id = vector<ll>(m+1);
        sz = vector<ll>(m+1, 1);
        iota(all(id), 0);
        vector<tuple<ll, ll, ll>> grafo;
        for (int i = 0; i < n; i++){
            ll a, b, w;
            cin >> a >> b >> w;
            grafo.emplace_back(w, a, b);
        }
        sort(all(grafo));
        cout << kruskal(grafo, m) << "\n";
    }
    return 0;
}
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

ll kruskal(vector<tuple<ll, ll, ll>> &grafo, ll n, string m){
    ll ans = 0;
    ll w, a, b;
    if (m == "menor"){
        for (auto i: grafo){
            tie(w, a, b) = i;
            if (find(a) != find(b)){
                unionn(a, b);
                ans += w;
            }
        }
    } else {
        for (int i = n-1; i >= 1; i--){
            tie(w, a, b) = grafo[i];
            if (find(a) != find(b)){
                unionn(a, b);
                ans += w;
            }
        }
    }
    return ans;
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    ll n;
    cin >> n;
    id = vector<ll>(n+1);
    sz = vector<ll>(n+1, 1);
    iota(all(id), 0);
    vector<tuple<ll, ll, ll>> grafo;
    for (int i = 0; i < n; i++){
        ll a, b, w;
        cin >> a >> b >> w;
        grafo.emplace_back(w, a, b);
    }
    sort(all(grafo));
    ll maior = kruskal(grafo, n, "maior");
    id = vector<ll>(n+1);
    sz = vector<ll>(n+1, 1);
    iota(all(id), 0);
    ll menor = kruskal(grafo, n, "menor");
    cout << maior << "\n";
    cout << menor << "\n";
    return 0;
}
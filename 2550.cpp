#include <bits/stdc++.h>

#define ll long long int
#define all(x) x.begin(), x.end()

using namespace std;


vector<ll> id, sz;

void dfs(vector<vector<int>> &adj, vector<bool> &vis, int x){
    vis[x] = true;
    for (auto i: adj[x]){
        if (!vis[i]){
            dfs(adj, vis, i);
        }
    }
}

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
    ll n, m;
    while (cin >> n >> m){
        id = vector<ll>(n+1);
        sz = vector<ll>(n+1, 1);
        iota(all(id), 0);
        ll a, b, w;
        vector<tuple<ll, ll, ll>> grafo;
        for (ll i = 0; i < m; i++){
            cin >> a >> b >> w;
            grafo.emplace_back(w, a, b);
        }
        sort(all(grafo));
        ll ans = 0;
        vector<vector<int>> adj(n+1, vector<int>());
        for (auto i: grafo){
            tie(w, a, b) = i;
            if (find(a) != find(b)){
                unionn(a, b);
                adj[a].push_back(b);
                adj[b].push_back(a);
                ans += w;
            }
        }
        vector<bool> vis(n+1, false);
        dfs(adj, vis, 1);
        bool possivel = true;
        for (int i = 1; i <= n; i++){
            if (!vis[i]){
                possivel = false;
                break;
            }
        }
        if (possivel) cout << ans << "\n";
        else cout << "impossivel" << "\n";
    }
    return 0;
}
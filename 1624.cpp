#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define all(x) x.begin(), x.end()

vector<pair<int, int>> a;
vector<vector<int>> memo;
int func(int w, int n){
    if (memo[w][n] != -1){
        return memo[w][n];
    }
    if (w == 0 || n == 0){
        return memo[w][n] = 0;
    }
    if (a[n-1].second > w){
        return memo[w][n] = func(w, n-1);
    }
    return memo[w][n] = max(func(w, n-1), a[n-1].first + func(w - a[n-1].second, n-1));
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n;
    while (true){
        cin >> n;
        if (!n) break;
        a.assign(n, {0,0});
        for (int i = 0; i < n; i++){
            cin >> a[i].first >> a[i].second;
        }
        int p;
        cin >> p;
        memo.assign(p+1, vector<int>(n+1, -1));
        sort(all(a));
        cout << func(p, n) << "\n";
    }
    return 0;
}
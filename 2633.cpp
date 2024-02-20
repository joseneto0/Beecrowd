#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define all(x) x.begin(),x.end()

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n;
    auto comp = [](pair<string, int> x, pair<string, int> y){
        return x.second < y.second;
    };
    while (cin >> n){
        vector<pair<string, int>> a(n);
        for (int i = 0; i < n; i++){
            cin >> a[i].first >> a[i].second;
        }
        sort(all(a), comp);
        for (int i = 0; i < a.size(); i++){
            if (i == a.size() - 1) cout << a[i].first;
            else cout << a[i].first << " ";
        }
        cout << "\n";
    }
    return 0;
}
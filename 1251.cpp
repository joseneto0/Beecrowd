#include <bits/stdc++.h>

#define ll long long int
#define all(x) x.begin(), x.end()

using namespace std;

bool cmp(pair<int, int> &x, pair<int, int> &y){
    if (x.second == y.second){
        return x.first > y.first;
    }
    return x.second < y.second;
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    string s;
    int cont = 0;
    while (cin >> s){
        if (cont > 0 )cout << "\n";
        map<int, int> mp;
        for (int i = 0; i < s.length(); i++){
            mp[int(s[i])]++;
        }
        vector<pair<int, int>> a;
        for (auto x: mp){
            a.push_back({x.first, x.second});
        }
        sort(all(a), cmp);
        for (auto x: a){
            cout << x.first << " " << x.second << "\n";
        }
        cont++;
    }
    return 0;
}
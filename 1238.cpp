#include <bits/stdc++.h>

#define ll long long int
#define all(x) x.begin(), x.end()

using namespace std;

void solve(){
    string s1, s2;
    cin >> s1 >> s2;
    vector<string> a(200);
    int j = 0;
    for (int i = 0; i < s1.size(); i++){
        a[j] = s1[i];
        j+= 2;
    }
    j = 1;
    for (int i = 0; i < s2.size(); i++){
        a[j] = s2[i];
        j += 2;
    }
    for (auto i : a){
        cout << i;
    }
    cout << "\n";
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int t;
    cin >> t;
    while (t--){
        solve();
    }
    return 0;
}
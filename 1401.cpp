#include <bits/stdc++.h>

#define ll long long int
#define all(x) x.begin(), x.end()

using namespace std;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int n;
    cin >> n;
    string s;
    vector<char> a;
    for (int i = 0; i < n; i++){
        cin >> s;
        for (char j: s){
            a.push_back(j);
        }
        sort(all(a));
        do {
            for (int i = 0; i < a.size(); i++){
                cout << a[i];
            }
            cout << "\n";
        } while (next_permutation(all(a)));
        a.clear();
        cout << "\n";
    }
    return 0;
}
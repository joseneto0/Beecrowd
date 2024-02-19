#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n, q, aux, teste = 1;
    while (true){
        cin >> n >> q;
        if (n == 0 && q == 0){
            break;
        }
        vector<int> a(n);
        for (int i = 0; i < n; i++){
            cin >> a[i];
        }
        sort(a.begin(), a.end());
        cout << "CASE# " << teste << ":" << "\n";
        for (int i = 0; i < q; i++){
            cin >> aux;
            int pos = lower_bound(a.begin(), a.end(), aux) - a.begin();
            if (a[pos] == aux){
                cout << aux << " found at " << pos+1 << "\n";
            } else {
                cout << aux << " not found" << "\n";
            }
        }
        teste++;
    }
    return 0;
}
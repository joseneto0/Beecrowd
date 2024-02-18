#include <bits/stdc++.h>

using namespace std;

int main(void){
    int t;
    vector<unsigned long long> v = {0, 1};
    cin >> t;
    while (t--){
        int n;
        cin >> n;
        v.clear();
        v = {0, 1};
        for (int i = 2; i <=n; i++){
            v.push_back(v[i-1] + v[i-2]);
        }
        cout << "Fib(" << n << ") = " << v[n] << '\n';
    }
}
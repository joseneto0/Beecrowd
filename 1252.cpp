#include <bits/stdc++.h>

#define ll long long int
#define all(x) x.begin(), x.end()

using namespace std;
int m;

bool cmp(int &x, int &y){
    if (x % 2 == 0 && y % 2 != 0 && x % m == y % m){
        return x % 2 != 0;
    }
    if (x % 2 != 0 && y % 2 == 0 && x % m == y % m){
        return y % 2 != 0;
    }
    if (x % 2 != 0 && y % 2 != 0 && x % m == y % m){
        return x > y;
    }
    if (x % 2 == 0 && y % 2 == 0 && x % m == y % m){
        return x < y;
    }
    return (x % m) < (y % m);
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int n;
    while (true){
        cin >> n >> m;
        cout << n << " " << m << "\n";
        if (n == 0 && m == 0){
            break;
        }
        vector<int> a(n);
        for (int i = 0; i < n; i++){
            cin >> a[i];
        }
        sort(all(a), cmp);
        for (auto i: a){
            cout << i << "\n";
        }
    }
    return 0;
}
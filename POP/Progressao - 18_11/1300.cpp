#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    int a;
    while (cin >> a){
        cout << ((a % 6 == 0) ? "Y" : "N") << "\n";
    }
    return 0;
}
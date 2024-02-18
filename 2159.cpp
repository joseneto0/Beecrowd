#include <bits/stdc++.h>

using namespace std;

int main(){
    long n;
    double p, m;
    cin >> n;
    p = n / log(n);
    m = p * 1.25506;
    cout << fixed << setprecision(1) << p << " " << m << endl;
    return 0;
}
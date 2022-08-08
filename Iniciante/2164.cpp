#include <bits/stdc++.h>
using namespace std;

int main(){
    int num;
    double fibbo;
    cin >> num;
    fibbo = ((pow(((1 + sqrt(5)) / 2), num)) - (pow(((1 - sqrt(5)) / 2), num))) / sqrt(5);
    cout << fixed << setprecision(1) << fibbo << endl;
    return 0;
}
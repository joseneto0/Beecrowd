#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    vector<int> v(20); vector<int> invertido(20);
    for (int i = 0; i < v.size(); i++){
        cin >> v[i];
    }
    int pos = 0;
    for (int j = 19; j >= 0; j--){
        invertido[pos] = v[j];
        pos += 1;
    }
    for (int i = 0; i < v.size(); i++){
        cout << "N[" << i << "] = " << invertido[i] << '\n';
    }
}

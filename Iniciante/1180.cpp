#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i =0; i < v.size(); i++){
        cin >> v[i];
    }
    int min = *min_element(v.begin(), v.end());
    int pos;
    for (int i = 0; i < v.size(); i++){
        if (v[i] == min){
            pos = i;
        }
    }
    cout << "Menor valor: " << min << '\n';
    cout << "Posicao: " << pos << '\n';
}

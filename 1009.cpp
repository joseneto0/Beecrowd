#include <bits/stdc++.h>

using namespace std;

int main()
{
    string nome;
    double salario, totalVendas;
    cin >> nome;
    cin >> salario;
    cin >> totalVendas;
    cout << fixed << setprecision(2);
    cout << "TOTAL = R$ " << salario + (0.15 * totalVendas)  << endl;
    return 0;
}

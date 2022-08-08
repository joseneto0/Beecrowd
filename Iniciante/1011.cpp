#include <bits/stdc++.h>

using namespace std;

int main()
{
    double raio, conta;
    cin >> raio;
    double raioResultado = pow(raio, 3);
    conta = (4.0/3) * 3.14159 * raioResultado;
    cout << fixed << setprecision(3);
    cout << "VOLUME = " << conta << endl;
    return 0;
}

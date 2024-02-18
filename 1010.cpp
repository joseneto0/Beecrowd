#include <bits/stdc++.h>

using namespace std;

int main()
{
    int cod1, numero1, cod2, numero2;
    double valor1, valor2;
    cin >> cod1 >> numero1 >> valor1;
    cin >> cod2 >> numero2 >> valor2;
    cout << fixed << setprecision(2);
    cout << "VALOR A PAGAR: R$ " << valor1 * numero1 + valor2 * numero2 << endl;
    return 0;
}

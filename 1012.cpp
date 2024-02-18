#include <bits/stdc++.h>

using namespace std;

int main()
{
    double A, B, C;
    double pi = 3.14159;
    cin >> A >> B >> C;
    cout << fixed << setprecision(3);
    cout << "TRIANGULO: " << (A * C) / 2 << "\nCIRCULO: " << pi * pow(C, 2) << "\nTRAPEZIO: " << (A + B) * C / 2 << "\nQUADRADO: " << pow(B, 2) << "\nRETANGULO: " <<A * B << endl;
    return 0;
}

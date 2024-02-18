#include <bits/stdc++.h>

using namespace std;

int main()
{
    int numFunc, horasTrab;
    double valorHora;
    cin >> numFunc;
    cin >> horasTrab;
    cin >> valorHora;
    cout << fixed << setprecision(2);
    cout << "NUMBER = " << numFunc << endl;
    cout << "SALARY = U$ " << horasTrab * valorHora << endl;
    return 0;
}

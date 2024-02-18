#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int valor, divisao;
    cin >> valor;
    cout << valor << endl;
    cout << valor / 100 << " nota(s) de R$ 100,00" << endl;
    divisao = valor % 100;
    cout << divisao / 50 << " nota(s) de R$ 50,00" << endl;
    divisao = divisao % 50;
    cout << divisao / 20 << " nota(s) de R$ 20,00" << endl;
    divisao = divisao % 20;
    cout << divisao / 10 << " nota(s) de R$ 10,00" << endl;
    divisao = divisao % 10;
    cout << divisao / 5 << " nota(s) de R$ 5,00" << endl;
    divisao = divisao % 5;
    cout << divisao / 2 << " nota(s) de R$ 2,00" << endl;
    divisao = divisao % 2;
    cout << divisao / 1 << " nota(s) de R$ 1,00" << endl;
    return 0;
}

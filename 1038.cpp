#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int codigo, quantidade;
    cin >> codigo >> quantidade;
    codigo -= 1;
    double lista[] = {4.00, 4.50, 5.00, 2.00, 1.50};
    cout << fixed << setprecision(2);
    cout << "Total: R$ " << lista[codigo] * quantidade << endl;
    return 0;
}

#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    double a, b, soma = 0;
    cin >> a >> b;
    a += 2;
    cout << fixed << setprecision(2) << b / a << endl;
    return 0;
}
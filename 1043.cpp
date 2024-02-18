#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    float a, b, c;
    cin >> a >> b >> c;
    cout << fixed << setprecision(1);
    if ((a < b+c) && (b < a+c) && (c < b+a)){
        cout << "Perimetro = " << a + b + c << endl;
    } else{
        cout << "Area = " << (a+b) * c / 2 << endl;
    }
    return 0;
}

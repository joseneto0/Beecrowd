#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    double a, b;
    cin >> a >> b;
    cout << fixed << setprecision(2) << (b/a - 1) * 100 << "%" << endl;
    return 0;
}

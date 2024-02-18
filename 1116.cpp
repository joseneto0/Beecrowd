#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int n;
    double x, y;
    cin >> n;
    for (int i=0; i<n; i++){
        cin >> x >> y;
        if (y == 0){
            cout << "divisao impossivel" << endl;
        } else {
            double divisao = x / y;
            cout << fixed << setprecision(1);
            cout << divisao << endl;
        }
    }
    return 0;
}
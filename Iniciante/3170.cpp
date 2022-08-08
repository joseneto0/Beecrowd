#include <iostream>

using namespace std;

int main(){
    int b, g;
    cin >> b >> g;
    if (g % 2 == 0){
        if (g/2 <= b){
            cout << "Amelia tem todas bolinhas!" << endl;
        } else {
            cout << "Faltam " << g/2 - b << " bolinha(s)" << endl;
        }
    } else{
        while (g % 2 != 0){
            g -= 1;
        }
        if (g/2 <= b){
            cout << "Amelia tem todas bolinhas!" << endl;
        } else {
            cout << "Faltam " << g/2 - b << " bolinha(s)" << endl;
        }
    }
    return 0;
}
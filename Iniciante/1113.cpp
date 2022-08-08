#include <iostream>

using namespace std;

int main(){
    int x, y;
    while (x != y){
        cin >> x >> y;
        if (x>y && x != y){
            cout << "Decrescente" << endl;
        } else if (y > x && x != y) {
            cout << "Crescente" << endl;
        }
    }
    return 0;
}
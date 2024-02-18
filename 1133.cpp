#include <iostream>

using namespace std;

int main(){
    int x, y, aux;
    cin >> x >> y;
    if (x<=y){
        x += 1;
        for (x; x<y; x++){
            if (x % 5 == 2 || x % 5 == 3){
                cout << x << endl;
            }
        }
    } else {
        y += 1;
        for (y; y<x; y++){
            if (y % 5 == 2 || y % 5 == 3){
                cout << y << endl;
            }
        }
    }
    return 0;
}

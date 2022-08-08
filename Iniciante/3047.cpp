#include <iostream>

using namespace std;

int main(){
    int m, a, b, c=0;
    cin >> m >> a >> b;
    c = m - (a+b);
    if (a > b && a > c){
        cout << a << endl;
    } else if (b > a && b > c){
        cout << b << endl;
    } else{
        cout << c << endl;
    }
    return 0;
}
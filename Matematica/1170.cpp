#include <iostream>

using namespace std;

int main(){
    int n, cont;
    double num;
    cin >> n;
    for (int i=0; i<n; i++){
        cin >> num;
        while (num > 1){
            num /= 2;
            cont ++;
        }
        cout << cont << " dias" << endl;
        cont = 0;
    }
    return 0;
}

#include <iostream>

using namespace std;

int main(){
    float valores;
    int contador;
    for (int i=0; i<6;i++){
        cin >> valores;
        if (valores > 0){
            contador += 1;
        }
    }
    cout << contador << " valores positivos" << endl;
    return 0;
}

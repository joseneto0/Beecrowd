#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int valores , maior, pos;
    for (int i=1; i<=100;i++){
        cin >> valores;
        if (maior < valores){
            maior = valores;
            pos = i;
        }
    }
    cout << maior << endl;
    cout << pos << endl;
    return 0;
}
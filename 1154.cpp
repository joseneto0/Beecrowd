#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    double idade=0, soma=0, aux=0;
    while (true){
        cin >> idade;
        if (idade < 0){
            break;
        }
        soma += idade;
        aux += 1;
    }
    cout << fixed << setprecision(2);
    cout << soma / aux << endl;
    return 0;
}

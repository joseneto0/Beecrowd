#include <iostream>

using namespace std;

int main(){
    int cod, alcool=0, gasolina=0, diesel=0;
    while (cod != 4){
        cin >> cod;
        switch (cod){
        case 1:
            alcool += 1;
            break;
        case 2:
            gasolina += 1;
            break;
        case 3:
            diesel += 1;
            break;
        default:
            continue;
        }

    }
    cout << "MUITO OBRIGADO" << endl << "Alcool: " << alcool << endl << "Gasolina: " << gasolina << endl << "Diesel: " << diesel << endl;
    return 0;
}
#include <iostream>

using namespace std;

int main(){
    int inicio, fim, duracao;
    cin >> inicio >> fim;
    duracao = fim - inicio;
    if (duracao <= 0){
        duracao += 24;
        cout << "O JOGO DUROU " << duracao << " HORA(S)" << endl;
    } else {
        cout << "O JOGO DUROU " << duracao << " HORA(S)" << endl;
    }
    return 0;
}

#include <bits/stdc++.h>

using namespace std;

int main(){
    int N, qntd;
    double pCoelho, pRatos, pSapos;
    double lista[3] = {};
    string tipo;
    cin >> N;
    for (int i=0; i<N; i++){
        cin >> qntd >> tipo;
        if (tipo == "C"){
            lista[0] += qntd;
        } else if (tipo == "R"){
            lista[1] += qntd;
        } else{
            lista[2] += qntd;
        }
    }
    pCoelho = (lista[0] * 100) / (lista[0] + lista[1] + lista[2]);
    pRatos = (lista[1] * 100 / (lista[0] + lista[1] + lista[2]));
    pSapos = (lista[2] * 100) / (lista[0] + lista[1] + lista[2]);
    cout << fixed << setprecision(0);
    cout << "Total: " << lista[0] + lista[1] + lista[2] << " cobaias" << endl;
    cout << "Total de coelhos: " << lista[0] << endl;
    cout << "Total de ratos: " << lista[1] << endl;
    cout << "Total de sapos: " << lista[2] << endl;
    cout << fixed << setprecision(2);
    cout << "Percentual de coelhos: " << pCoelho << " %" << endl;
    cout << "Percentual de ratos: " << pRatos << " %" << endl;
    cout << "Percentual de sapos: " << pSapos << " %" << endl;
    return 0;
}
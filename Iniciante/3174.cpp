#include <iostream>
#include <string>

using namespace std;

int main(){
    int n, h, somaBonecos = 0, somaArquitetos = 0, somaMusicos = 0, somaDesenhistas = 0;
    string e, g;
    cin >> n;
    for (int i = 0; i<n; i++){
        cin >> e >> g >> h;
        if (g == "bonecos"){
            somaBonecos += h;
        } else if (g == "arquitetos"){
            somaArquitetos += h;
        } else if (g == "musicos"){
            somaMusicos += h;
        } else {
            somaDesenhistas += h;
        }
    }
    cout << (somaBonecos / 8) + (somaArquitetos / 4) + (somaMusicos / 6) + (somaDesenhistas / 12) << endl;
    return 0;
}
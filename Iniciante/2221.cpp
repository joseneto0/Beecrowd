#include <iostream>

using namespace std;

int main(){
    int t, b, a1, d1, l1, a2, d2, l2, valorGolpe_guarte, valorGolpe_dabriel;
    cin >> t;
    for (int i=0; i<t; i++){
        cin >> b;
        cin >> a1 >> d1 >> l1;
        cin >> a2 >> d2 >> l2;
        valorGolpe_dabriel = (a1 + d1) / 2;
        if (l1 % 2 == 0){
            valorGolpe_dabriel += b;
        }
        valorGolpe_guarte = (a2 + d2) / 2;
        if (l2 % 2 == 0){
            valorGolpe_guarte += b;
        }
        if (valorGolpe_dabriel > valorGolpe_guarte){
            cout << "Dabriel" << endl;
        } else if (valorGolpe_guarte > valorGolpe_dabriel){
            cout << "Guarte" << endl;
        } else {
            cout << "Empate" << endl;
        }
    }
    return 0;
}

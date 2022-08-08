#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    double tempo, velocidadeMedia;
    cin >> tempo;
    cin >> velocidadeMedia;
    cout << fixed << setprecision(3);
    cout << (tempo * velocidadeMedia) / 12 << endl;
    return 0;
}

#include <iostream>
#include <string>

using namespace std;

int main(){
    string nomes[10];
    for (int i=0;i<10;i++){
        cin >> nomes[i];
    }
    cout << nomes[2] << endl;
    cout << nomes[6] << endl;
    cout << nomes[8] << endl;
    return 0;
}
#include <iostream>

using namespace std;

int main(){
    int n, valores;
    cin >> n;
    for (int i = 0; i<n; i++){
        cin >> valores;
        cout << "resposta " << i+1 << ": " << valores << endl;
    }
    return 0;
}
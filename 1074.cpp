#include <iostream>

using namespace std;

int main(){
    int N, valores;
    cin >> N;
    for (int i = 0; i<N; i++){
        cin >> valores;
        if (valores % 2 == 0 && valores > 0){
            cout << "EVEN POSITIVE" << endl;
        } else if (valores % 2 == 0 && valores < 0){
            cout << "EVEN NEGATIVE" << endl;
        } else if (valores % 2 != 0 && valores > 0){
            cout << "ODD POSITIVE" << endl;
        } else if (valores % 2 != 0 && valores < 0){
            cout << "ODD NEGATIVE" << endl;
        } else if (valores == 0){
            cout << "NULL" << endl;
        }
    }
    return 0;
}
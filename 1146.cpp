#include <iostream>

using namespace std;

int main(){
    int num;
    while (num != 0){
        cin >> num;
        for (int i=1; i<=num; i++){
            if (i < num){
                cout << i << " ";
            } else {
                cout << i << endl;
            }
        }
    }
    return 0;
}

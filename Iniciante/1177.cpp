#include <iostream>

using namespace std;

int main(){
    int T=0,N[1000], j=0;
    cin >> T;
    for (int i = 0; i<1000; i++){
        cout << "N[" << i << "] = " << j << endl;
        j++;
        if (j == T){
            j = 0;
        }
    }
    return 0;
}

#include <iostream>

using namespace std;

int main(){
    int i = 1, j = 7;
    for (i; i<=9; j-=1){
        cout << "I=" << i << " J=" << j << endl;
        if (j==5){
            i += 2;
            j = 8;
        }
    }
    return 0;
}

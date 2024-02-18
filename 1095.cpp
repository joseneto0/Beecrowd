#include <iostream>

using namespace std;

int main(){
    int i = 1, j = 60;
    for (i; j>=0; j-=5){
        cout << "I=" << i << " J=" << j << endl;
        i += 3;
    }
    return 0;
}

#include <iostream>

using namespace std;

int main(){
    int n, i, j, k;
    cin >> n;
    for (i=1; i<=n; i++){
        j = i * i;
        k = i * i * i;
        cout << i << " "  << j << " " << k << endl;
    }
    return 0;
}

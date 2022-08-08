#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int N;
    float n1, n2, n3;
    cin >> N;
    cout << fixed << setprecision(1);
    for (int i = 0; i<N; i++){
        cin >> n1 >> n2 >> n3;
        cout << ((n1 * 2) + (n2 * 3) + (n3 * 5)) / (2+3+5) << endl;
    }
    return 0;
}
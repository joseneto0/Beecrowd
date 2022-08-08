#include <iostream>

using namespace std;

int main(){
    int primeiro = 0, segundo = 1, aux, n;
    cin >> n;
    if (n == 0){
        exit(0);
    }else if (n == 1){
        cout << primeiro << endl;
    }else if (n == 2){
        cout << primeiro << " " << segundo << endl;
    }else {
        n -= 2;
        cout << primeiro << " " << segundo << " ";
        for (int i=1;i<=n;i++){
            aux = primeiro + segundo;
            if (i < n){
                cout << aux << " ";
            } else if (i == n) {
                cout << aux << endl;
            }
            primeiro = segundo;
            segundo = aux;
        }
    }
    return 0;
}

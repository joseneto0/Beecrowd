#include <iostream>
#include <string>

using namespace std;

int main(){
    string palavra;
    cin >> palavra;
    string resposta = (palavra.size() >= 10) ? "palavrao" : "palavrinha";
    cout << resposta << endl;
    return 0;
}
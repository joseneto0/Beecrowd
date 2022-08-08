#include <iostream>

using namespace std;

int main(){
    int segundos, h, m, s;
    cin >> segundos;
    h = segundos / 3600;
    m = (segundos%3600) / 60;
    s = segundos % 60;
    cout << h << ":" << m << ":" << s << endl;
    return 0;
}

#include <bits/stdc++.h>

using namespace std;

int main(){
    double total_s=0, acertos_s=0, total_b=0, acertos_b=0, total_a=0, acertos_a=0, s, b, a, s1, b1, a1, n;
    string nome;
    cin >> n;
    for (int i = 0; i<n; i++){
        cin >> nome;
        cin >> s >> b >> a;
        cin >> s1 >> b1 >> a1;
        total_s += s; total_b += b; total_a += a; acertos_s += s1; acertos_b += b1; acertos_a += a1;
    }
    cout << fixed << setprecision(2);
    cout << "Pontos de Saque: " << acertos_s * 100 / total_s << " %." << endl;
    cout << "Pontos de Bloqueio: " << acertos_b * 100 / total_b << " %." << endl;
    cout << "Pontos de Ataque: " << acertos_a * 100 / total_a << " %." << endl;
    return 0;
}

#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    float nota1, nota2, nota3, nota4, notaExame, media;
    cin >> nota1 >> nota2 >> nota3 >> nota4;
    media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4) + (nota4 * 1)) / (2 + 3 + 4 + 1);
    cout << fixed << setprecision(1);
    cout << "Media: "<< media << endl;
    if (media >= 7.0){
        cout << "Aluno aprovado." << endl;
    } else if (media >= 5.0 && media <= 6.9){
        cout << "Aluno em exame." << endl;
        cin >> notaExame;
        cout << "Nota do exame: " << notaExame << endl;
        media = (media + notaExame) / 2;
        if (notaExame >= 5.0){
            cout << "Aluno aprovado." << endl;
            cout << "Media final: " << media << endl;
        } else {
            cout << "Aluno reprovado." << endl;
            cout << "Media final: " << media << endl;
        }
    } else {
        cout << "Aluno reprovado." << endl;
    }

    return 0;
}

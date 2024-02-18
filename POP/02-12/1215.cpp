//lista
#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    string s, palavra_atual;
    set<string> palavras;
    string alfabeto = "abcdefghijklmnopqrstuvwxyz";
    while (cin >> s){
        stringstream ss(s);
        string word;
        while (ss >> palavra_atual){
            for (auto x: palavra_atual){
                if (alfabeto.find(tolower(x)) != string::npos && x != ' ' && x != '\n'){
                    word += tolower(x);
                } else {
                    if (word != "") palavras.insert(word);
                    word = "";
                }
            }
            if (word != ""){
                palavras.insert(word);
            }   
        }
    }
    for (auto x: palavras){
        cout << x << "\n";
    }
    return 0;
}
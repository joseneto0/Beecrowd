#include <iostream>

using namespace std;

int main(){
    int H, E, A, O, W, X;
    cin >> H >> E >> A >> O >> W >> X;
    if (H + E + A > O + W || H + E + A + X > O + W){
        cout << "Middle-earth is safe." << endl;
    } else {
        cout << "Sauron has returned." << endl;
    }
    return 0;
}
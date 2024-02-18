#include <iostream>
#include <string>

using namespace std;

int main(){
    int h, z, l;
    string meio;
    cin >> h >> z >> l; 
    if (h > z && h > l && z < l){
        meio = "luisinho";
    } else if (h > z && h > l && z > l){
        meio = "zezinho";
    }else if (z > h && z > l && h > l){
        meio = "huguinho";
    } else if (z > h && z > l && l > h){
        meio = "luisinho";
    } else if (l > h && l > z && h > z){
        meio = "huguinho";
    } else if (l > h && l > z && z > h){
        meio = "zezinho";
    }
    cout << meio << endl;
    return 0;
}
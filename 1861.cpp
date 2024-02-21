#include <bits/stdc++.h>

#define ll long long int
#define all(x) x.begin(), x.end()

using namespace std;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
    string a1, a2;
    map<string, int> mp1, mp2;
    while (cin >> a1 >> a2){
        mp1[a1]++;
        mp2[a2]++;
    }
    cout << "HALL OF MURDERERS" << "\n";
    map<string, int> :: iterator it;
    for (it = mp1.begin(); it != mp1.end(); it++){
        int aux = mp2[it->first];
        if (!aux) cout << it->first << " " << it->second << "\n";
    }
    return 0;
}
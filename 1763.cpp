#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define all(x) x.begin(),x.end()

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    string s;
    map<string, string> mp;
    mp["brasil"] = "Feliz Natal!";
    mp["alemanha"] = "Frohliche Weihnachten!";
    mp["austria"] = "Frohe Weihnacht!";
    mp["coreia"] = "Chuk Sung Tan!";
    mp["espanha"] = "Feliz Navidad!";
    mp["grecia"] = "Kala Christougena!";
    mp["estados-unidos"] = "Merry Christmas!";
    mp["inglaterra"] = "Merry Christmas!";
    mp["australia"] = "Merry Christmas!";
    mp["portugal"] = "Feliz Natal!";
    mp["suecia"] = "God Jul!";
    mp["turquia"] = "Mutlu Noeller";
    mp["argentina"] = "Feliz Navidad!";
    mp["chile"] = "Feliz Navidad!";
    mp["mexico"] = "Feliz Navidad!";
    mp["antardida"] = "Merry Christmas!";
    mp["canada"] = "Merry Christmas!";
    mp["irlanda"] = "Nollaig Shona Dhuit!";
    mp["belgica"] = "Zalig Kerstfeest!";
    mp["italia"] = "Buon Natale!";
    mp["libia"] = "Buon Natale!";
    mp["siria"] = "Milad Mubarak!";
    mp["marrocos"] = "Milad Mubarak!";
    mp["japao"] = "Merii Kurisumasu!";
    while (cin >> s){
        if (mp.find(s) != mp.end()){
            cout << mp[s] << "\n";
        } else {
            cout << "--- NOT FOUND ---" << "\n";
        }
    }
    return 0;
}
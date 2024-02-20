#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define all(x) x.begin(),x.end()


int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int h1, m1, h2, m2;
    while (true){
        cin >> h1 >> m1 >> h2 >> m2;
        if (h1 == 0 && m1 == 0 && h2 == 0 && m2 == 0){
            break;
        }
        int ans = 0;
        while (true){
            if (h1 == h2 && m1 == m2){
                break;
            } 
            if (m1 < 60){
                m1++;
                ans++;
            }
            if (m1 == 60){
                h1++;
                m1 = 0;
            }
            if (h1 > 23){
                h1 = 0;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}
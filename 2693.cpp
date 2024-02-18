#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int q;
    while (cin >> q){
        string s;
        char dir;
        int w;
        vector<tuple<string, char, int>> tp;
        for (int i = 0; i < q; i++){
            cin >> s >> dir >> w;
            tp.push_back(make_tuple(s, dir ,w));
        }
        auto comp = [](tuple<string, char, int> x, tuple<string, char, int> y){
            if (get<2>(x) == get<2>(y)){
                if (get<1>(x) == get<1>(y)){
                    return get<0>(x) < get<0>(y);
                }
                return get<1>(x) < get<1>(y);
            }
            return get<2>(x) < get<2>(y);
        };

        sort(tp.begin(), tp.end(), comp);
        for (auto x: tp){
            tie(s, dir, w) = x;
            cout << s << "\n";
        }
    }
    return 0;
}
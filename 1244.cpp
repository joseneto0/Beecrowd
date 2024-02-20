#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define all(x) x.begin(),x.end()

bool cmp(string &a, string &b){
    return a.length() > b.length();
}

template <class T>
void insertionSort(vector<T> &a){
    int n = a.size();
    for (int i = 0; i < n; i++){
        int j = i, k = j-1;
        while (k > -1 && cmp(a[j], a[k])){
            swap(a[k], a[j]);
            j--; 
            k--;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n;
    cin >> n;
    cin.ignore();
    string s, aux;
    stringstream x;
    vector<string> a;
    for (int i = 0; i < n; i++){
        getline(cin, s);
        x << s;
        while (x >> aux){
            a.push_back(aux);
        }
        insertionSort(a);
        cout << a[0];
        for (int i = 1; i < a.size(); i++){
            cout << " " << a[i];
        }
        cout << "\n";
        a.clear();
        x.clear();
    }
    return 0;
}
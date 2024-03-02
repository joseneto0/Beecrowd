#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define all(x) x.begin(),x.end()

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int n;
    cin >> n;
    stack<char> st;
    char a, b, c, d, p, s, t, q;
    int cont = 0;
    while (n--){
        if (st.empty()){
            st.push('F');
            st.push('A');
            st.push('C');
            st.push('E');
        }
        cin >> a >> b >> c >> d;
        p = st.top();
        st.pop();
        s = st.top();
        st.pop();
        t = st.top();
        st.pop();
        q = st.top();
        st.pop();
        if (a == p && b == s && c == t && d == q){
            cont++;
        } else {
            st.push(q);
            st.push(t);
            st.push(s);
            st.push(p);
            st.push(a);
            st.push(b);
            st.push(c);
            st.push(d);
        }
    }
    cout << cont << "\n";
    return 0;
}
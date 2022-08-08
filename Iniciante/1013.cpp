#include <iostream>

using namespace std;

int main()
{
    int a, b, c, maiorAB;
    cin >> a >> b >> c;
    maiorAB = (a + b + abs(a-b)) / 2;
    maiorAB = (c + maiorAB + abs(maiorAB - c)) / 2;
    cout << maiorAB << " eh o maior" << endl;
    return 0;
}

#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

string getBinary(double number) {
    if (number <= 0 or number >= 1) {
        return "ERROR";
    }

    string s = ".";
    while (number > 0) {
        if (s.size() > 32) {
            return "ERROR";
        }

        double r = number * 2;
        if (r >= 1) {
            s += '1';
            number = r - 1;
        } else {
            s += '0';
            number = r;
        }
    }

    return s;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 

    for (int i = 0; i < 1000; i++) {
        double number = i / 1000.;
        string str = getBinary(number);

        if (str != "ERROR") {
            cout << number << " in binary representation = " << str << "\n";
        }
    }


    return 0;
}
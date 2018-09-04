/*
    * Cracking the coding interview Edition 6
    * Problem 1.3 URLify --> Replace all the spaces in a string with '%20'. 
    * Assumption : We have enough space to accomodate addition chars
    * Preferebly in place
*/

#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

void URLify(string& s, const int len) {
    int space = 0;
    for (char c : s) {
        if (c == ' ') {
            space++;
        }
    }

    int i = (int)s.size() - 1;
    for (int j = len - 1; j >= 0; j--) {
        if (s[j] != ' ') {
            s[i--] = s[j];
        } else {
            s[i--] = '0';
            s[i--] = '2';
            s[i--] = '%';
        }
    }
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    string s = "Mr John Smith    ";
    
    cout << "Actual string: " << s << "\n";
    URLify(s, 13);
    cout << "URLified string: " << s << "\n";


    return 0;
}
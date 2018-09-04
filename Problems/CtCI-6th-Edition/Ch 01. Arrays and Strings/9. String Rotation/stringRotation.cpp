#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

bool isSubstring(const string& s1, const string& s2) {
    return s2.find(s1) != string::npos;
}

bool isRotate(string s1, string s2) {
    s2 += s2;
    return isSubstring(s1, s2);
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    vector<string> s1 = {"abcde", "hello", "good", "cat"};
    vector<string> s2 = {"eabcd", "ehollo", "doog", "tca"};

    for (int i = 0; i < (int)s1.size(); i++) {
        if (isRotate(s1[i], s2[i])) {
            cout << s1[i] << " rotate => " << s2[i] << "\n";
        } else {
            cout << s1[i] << " wrong rotate => " << s2[i] << "\n";
        }
    }

    return 0;
}
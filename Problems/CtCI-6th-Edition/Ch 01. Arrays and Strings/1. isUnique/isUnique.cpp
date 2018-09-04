#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

// O(N) by time, O(1) by space
bool isUniqueChars(const string& s) {
    if (s.empty()) {
        return true;
    }

    vector<bool> counter(256, false);
    for (char c : s) {
        if (counter[c]) {
            return false;
        }

        counter[c] = true;
    }

    return true;
}

// O(N) by time, O(1) by space
bool isUniqueChars_bits(const string& s) {
    bitset<256> bits(0);

    for (char c : s) {
        if (bits.test(c) > 0) {
            return false;
        }

        bits.set(c);
    }

    return true;
}

// O(N^2) by time, O(1) by space
bool isUniqueChars_square(const string& s) {
    if (s.empty()) {
        return true;
    }

    for (int i = 0; i < (int)s.size() - 1; i++) {
        for (int j = i + 1; j < (int)s.size(); j++) {
            if (s[i] == s[j]) {
                return false;
            }
        }
    }

    return true;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 

    vector<string> words = {"hello", "world", "cpp", "algorithms", "string", "unique"};
    for (string word : words) {
        if (isUniqueChars(word)) {
            cout << word << ", chars unique\n";
        } else {
            cout << word << ", chars not unique\n";
        }
    }

    return 0;
}

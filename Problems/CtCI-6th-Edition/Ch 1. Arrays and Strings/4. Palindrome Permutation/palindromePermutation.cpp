#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

int getValue(const char& c) {
    int result = -1;
    if ('a' <= c and c <= 'z') {
        result = (c - 'a');
    } else if ('A' <= c and c <= 'Z') {
        result = (c - 'A');
    }

    return result;
}

// O(N) by time, O(1) by space
bool isPalindrome(const string& s) {
    vector<int> data(26, 0);
    int counter = 0;

    for (char c : s) {
        int value = getValue(c);
        if (value != -1) {
            data[value]++;

            if (data[value] & 1) {
                counter++;
            } else {
                counter--;
            }
        }
    }

    return counter <= 1;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    string s = "Tact Coa";
    vector<string> permutations = {"taco cat", "atco cta"};

    for (string permutation : permutations) {
        if (isPalindrome(permutation)) {
            cout << permutation << ", palindromic permutation of " << s << "\n";
        } else {
            cout << permutation << ", not palindromic permutation of " << s << "\n";
        }
    }


    return 0;
}
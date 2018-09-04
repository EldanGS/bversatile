#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

// O(N) by time, O(const) by space
bool checkPermutation(const string& s1, const string& s2) {
    if (s1.size() != s2.size()) {
        return false;
    }

    unordered_map<char, int> data;
    for (char c : s1) {
        data[c]++;
    }

    for (char c : s2) {
        data[c]--;
        if (data[c] < 0) {
            return false;
        }
    }

    return true;
}

// O(NlogN) by time, O(1) by space
bool checkPermutation_sort(string s1, string s2) {
    int n1 = (int)s1.size();
    int n2 = (int)s2.size();
    if (n1 != n2) {
        return false;
    }

    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());

    for (int i = 0; i < n1; i++) {
        if (s1[i] != s2[i]) {
            return false;
        }
    }

    return true;
}


int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    vector<string> s1 = {"abc", "wqrs", "google", "cpp", "fb", "foobar"};
    vector<string> s2 = {"cba", "wxsr", "ogolex", "pcp", "bf", "barfo"};

    for (int i = 0; i < (int)s1.size(); i++) {
        if (checkPermutation(s1[i], s2[i])) {
            cout << s1[i] << " permutation is " << s2[i] << "\n";
        } else {
            cout << s1[i] << " not permutation is " << s2[i] << "\n";
        }
    }


    return 0;
}
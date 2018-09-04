#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

// O(N) by time, O(1) by space
bool oneAway(const string& s1, const string& s2) {
    if (abs(s1.size() - s2.size()) > 1) {
        return false;
    }

    if (s1.size() < s2.size()) {
        oneAway(s2, s1);
    }

    vector<int> data(256, 0);
    for (char c : s2) {
        data[c]++;
    }

    int counter = 0;
    for (char c : s1) {
        data[c]--;
        if (data[c] < 0) {
            counter++;
        }
    }

    return (counter == 1);
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    vector<string> s1 = {"pale", "pales", "palse", "ple"};
    vector<string> s2 = {"pal", "pale", "bale", "bke"};

    int n = (int)s1.size();
    for (int i = 0; i < n; i++) {
        if (oneAway(s1[i], s2[i])) {
            cout << s1[i] << ", " << s2[i] << " -> " << "true\n"; 
        } else {
            cout << s1[i] << ", " << s2[i] << " -> " << "false\n"; 
        }
    }

    return 0;
}
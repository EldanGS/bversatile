#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

// O(N) by time, O(N) by space
string compression(string& s) {
    if (s.size() < 2) {
        return s;
    }
    
    string result =s.front();
    int n = (int)s.size();
    int count = 1;
    
    for (int i = 1; i < n; i++) {
        if (s[i] == s[i - 1]) {
            count++;
        } else {
            result += to_string(count);
            result += s[i];
            count = 1;
        }
    }
    result += to_string(count);

    return result;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    vector<string> data = {"aaabcd", "aaabbbcccddd", "abbbbbbbcd", "aabbccdd", "aabcccccaaa"};
    for (string text : data) {
        cout << text << " -> " << compression(text) << "\n";
    }


    return 0;
}
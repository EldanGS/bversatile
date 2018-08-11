// "Brevity is the soul of wit."
#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define pb push_back
#define ull unsigned long long

typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;

int main() { boost
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif  
    string s;
    getline(cin, s);
    {
        vector<char> temp;
        temp.push_back(' ');
        for (char& c : s) {
            temp.push_back(c);
            temp.push_back(' ');
        }
        s = string(temp.begin(), temp.end());
    }

    int n = (int)s.size();
    vector<int> dp(n, 0);
    int left = 0, right = 0;
    for (int i = 1; i < n; i++) {
        int L, R;

        if (i > right) {
            L = i;
            R = i;
        } else {
            assert((right + left) / 2 < i);
            int mi = right + left - i;
            L = i - dp[i] + 1;
            R = i + dp[i] - 1;

            if (R > right) {
                int d = R - right;
                R -= d;
                L += d;
            }
        }

        while (L - 1 >= 0 and R + 1 < n and s[L - 1] == s[R + 1]) {
            L--;
            R++;
        }

        dp[i] = R - i + 1;
        if (R > right) {
            left = L;
            right = R;
        }
    }

    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += dp[i] / 2;
    }

    cout << sum << "\n";

    return 0;
}

#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

int getPath(int n, int m) {
    vector<vector<int> > dp(n + 1, vector<int>(m + 1));
    dp[0][1] = dp[1][0] = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i == 0 and j == 0) continue;
            if (i == 0) {
                dp[i][j] = dp[i][j - 1];
            } else if (j == 0) {
                dp[i][j] == dp[i - 1][j];
            } else {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
    }

    return dp[n - 1][m - 1];
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 



    return 0;
}
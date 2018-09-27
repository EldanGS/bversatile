#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

long long tripleStep_naive(int n) {
    if (n < 0) {
        return 0;
    } else if (n == 0) {
        return 1;
    } else {
        return tripleStep_naive(n - 1) + tripleStep_naive(n - 2) + tripleStep_naive(n - 3);
    }
}

long long tripleStep_memo(int n, vector<int> memo) {
    if (n < 0) {
        return 0;
    } else if (n == 0) {
        return 1;
    } else if (memo[n] != -1) {
        return memo[n];
    } else {
        memo[n] = tripleStep_memo(n - 1, memo) + tripleStep_memo(n - 2, memo) + tripleStep_memo(n - 3, memo);

        return memo[n];
    }
}

long long tripleStep_iter(int n) {
    vector<int> dp(n);
    dp[0] = 1;
    dp[1] = 2;
    dp[2] = 4;
    for (int i = 3; i < n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    }

    return dp[n - 1];
}

long long tripleStep_optimal(int n) {
    if (n < 0) {
        return 0;
    } else if (n < 3) {
        return n;
    }

    int a = 1, b = 2, c = 4;
    for (int i = 3; i < n; i++) {
        int val = a + b + c;
        a = b;
        b = c;
        c = val;
    }

    return c;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    
    for (int i = 1; i <= 10; i++) {
        cout << "\nN = " << i << "\n";
        cout << "Triple Step naive Recursion: " << tripleStep_naive(i) << "\n";
        cout << "Triple Step Recursion with memo: " << tripleStep_memo(i, vector<int>(i + 1, -1)) << "\n";
        cout << "Triple Step iteration DP: " << tripleStep_iter(i) << "\n";
        cout << "Triple Step optimal memory: " << tripleStep_optimal(i) << "\n";
    }


    return 0;
}
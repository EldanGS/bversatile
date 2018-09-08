#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

// NAIVE Algorithm
string to_bit(int x) {
    string result = "";

    while (x > 0) {
        result += (x & 1) + '0';
        x >>= 1;
    }

    reverse(result.begin(), result.end());
    return result;
}

int flipToWin_brute(int num) {
    string str = to_bit(num);
    int answer = 0;

    for (int i = 0, k = 0; i < (int)str.size(); i++) {
        char c = str[i];
        if (c == '0') {
            str[i] = '1';
        }

        int current = 0;
        for (int j = 0; j < (int)str.size(); j++) {
            if (str[j] - '0') {
                current++;
            } else {
                current = 0;
            }
            answer = max(answer, current);
        }

        str[i] = c;
    }

    return min(answer, numeric_limits<int>::max());
}

// Effective Algortihm
int flipToWin(int num) {
    int result = 1;
    int lenLeft = 0, lenRight = 0;

    while (num > 0) {
        if (num & 1) {
            lenLeft++;
        } else {
            lenRight = lenLeft;
            lenLeft = 0;
        }
        num >>= 1;

        result = max(result, lenLeft + 1 + lenRight);
    }

    return min(result, numeric_limits<int>::max());
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 

    for (int num = 0; num < 100; num++) {
        cout << "number = " << num << ", bit representation = " << to_bit(num) << "\n";
        cout << "result brute = " << flipToWin_brute(num) << "\n";
        cout << "result effective = " << flipToWin(num) << "\n";
    }
    

    return 0;
}
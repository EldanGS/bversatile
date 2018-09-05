#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

int Insertion(int n, int m, int i, int j) { // 1000000
    // 31 lengths of bits ones, ones = 11111111
    int ones = ~0;

    // left = 11100000
    int left = ones << (j + 1);

    // right = 00000011
    int right = (1 << i) - 1;

    // mask is range of j to i, mask = 11100011
    int mask = left | right;

    int nCleared = n & mask;
    int mShifted = m << i;

    return nCleared | mShifted;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 

    cout << Insertion(100, 10, 2, 6) << "\n";


    return 0;
}
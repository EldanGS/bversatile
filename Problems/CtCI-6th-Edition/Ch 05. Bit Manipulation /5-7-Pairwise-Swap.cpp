#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

int pairwiseSwap(int n) {
    // 0101010101
    int evenMask = 0xAAAAAAAA; // assumes 32-bit integer
    // 1010101010
    int oddMask =  0x55555555; // assumes 32-bit integer

    return ((n & evenMask) >> 1) | ((n & oddMask) << 1);
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 

    /*
        Example 1:
        n = 5 = 101 
        even_mask = 010
        odd_mask = 101

        (n & even_mask) >> 1 = (5 & 2) >> 1 = 0 / 2 = 0
        (n & odd_mask) << 1 = (5 & 5) << 1 = 5 * 2 = 10

        0000
        |
        1010
        =
        1010 = 10
    */
    cout << pairwiseSwap(5) << "\n"; 


    return 0;
}
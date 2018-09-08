#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

int conversion(int a, int b) {
    return __builtin_popcount((a ^ b));
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 

    cout << conversion(29, 15) << "\n";

    return 0;
}
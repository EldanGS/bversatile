#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

bool debugger(int n) { 
    /*
        This method checkout if given N is power of two or not.

        Example 1:
        n = 8 = 1000
        n - 1 = 7 = 0111
        
        func: n & (n - 1) = 0; 
        conclusion: n(8) power of two

        Example 2:
        n = 6 = 0110
        n - 1 = 5 = 0101

        func: n & (n - 1) = 1
        conclusion: n(6) not power of two
        ___
        To sum up, number which is power of two has only 1 bit on the representation.
    */
    return (n & (n - 1)) == 0;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 

    for (int i = 1; i <= 100; i++) {
        if (debugger(i)) {
            cout << "number = " << i << ", power of two\n";
        }
    }    


    return 0;
}
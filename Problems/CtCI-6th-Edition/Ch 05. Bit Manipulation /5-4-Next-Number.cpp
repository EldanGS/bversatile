#include <bits/stdc++.h>
#include "Bit_Manipulations.h"

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

// NAIVE Algorithm
void nextNumber_naive(int number) {
    int smallest = number - 1;
    int largest = number + 1;

    int bcount = __builtin_popcount(number);
    while (smallest > INT_MIN + 1 and __builtin_popcount(smallest) != bcount) {
        smallest--;
    } 
    while (largest + 1 < INT_MAX and __builtin_popcount(largest) != bcount) {
        largest++;
    }

    cout << "Number is " << number << "\n";
    cout << "Next largest " << (largest + 1 == INT_MAX ? number : largest) << "\n";
    cout << "Next smallest " << (smallest == INT_MIN + 1 ? number : smallest) << "\n";
}

// Effective Algorithm, Get Next Largest Number
int nextLargestNumber(int number) {
    int c = number;
    int c0 = 0, c1 = 0;
    while ((c & 1) == 0 and c > 0) {
        c0++;
        c >>= 1;
    }
    while ((c & 1) and c > 0) {
        c1++;
        c >>= 1;
    }

    // if count of bits 31, there is no bigger number with same 1s
    if (c0 + c1 == 31 or c0 + c1 == 0) {
        return -1;
    }

    int p = c0 + c1; // position of rightmost non-trailing zero

    number |= (1 << p); // Flip rightmost non-trailing zero
    number &= ~((1 << p) - 1); // Clear all bits to the right of p
    number |= (1 << (c1 - 1)) - 1; // Insert (c1 - 1) ones on the right

    return number;
}

// Effective Algorithm, Get Previous Smallest Number
int previousSmallestNumber(int number) {
    int c = number;
    int c1 = 0, c0 = 0;

    while (c & 1) {
        c1++;
        c >>= 1;
    }
    
    if (c == 0) {
        return -1;
    }

    while (c > 0 and !(c & 1)) {
        c0++;
        c >>= 1;
    }

    int p = c0 + c1;
    number &= ((~0) << (1 << p + 1)); // clears from bit p onwards

    int mask = (1 << (c1 + 1)) - 1; // Sequence of (c1 + 1) ones
    number |= mask << (c0 - 1);

    return number;
}

// Arithmetic solution get next 
int getNextArith(int n) {
    int c = n;
    int c0 = 0, c1 = 0;
    while ((c & 1) == 0 and c > 0) {
        c0++;
        c >>= 1;
    }
    while ((c & 1) and c > 0) {
        c1++;
        c >>= 1;
    }

    return n + (1 << c0) + (1 << (c1 - 1)) - 1;
}

// Arithmetic solution get previous
int getPrevArith(int n) {
    int c = n;
    int c1 = 0, c0 = 0;

    while (c & 1) {
        c1++;
        c >>= 1;
    }
    
    if (c == 0) {
        return -1;
    }

    while (c > 0 and !(c & 1)) {
        c0++;
        c >>= 1;
    }

    return n - (1 << c1) - (1 << (c0 - 1)) + 1;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 

    for (int i = 0; i < 100; i++) {
        cout << "\n";
        cout << "Current number = " << i << "\n";
        cout << "Next Largest number = " << nextLargestNumber(i) << "\n";
        cout << "Previous Smallest number = " << previousSmallestNumber(i) << "\n";
    }

    

    return 0;
}
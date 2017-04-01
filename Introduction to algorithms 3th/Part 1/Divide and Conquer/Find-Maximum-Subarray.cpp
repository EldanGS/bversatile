#include <stdio.h>
#include <limits.h>
// #include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define frp freopen("input.txt", "r", stdin); \
            freopen("output.txt", "w", stdout); 

int max(int a, int b) { return (a > b)? a : b; }

int max(int a, int b, int c) { return max(max(a, b), c); }

int maxCrossingSum(int a[], int low, int mid, int high) {
    int leftSum = INT_MIN;
    int curSum = 0;
    for (int i = mid; i >= 0; i--) {
        curSum += a[i];

        if (leftSum < curSum) {
            leftSum = curSum;
        }
    }

    int rightSum = INT_MIN;
    curSum = 0;
    for (int i = mid + 1; i <= high; i++) {
        curSum += a[i];

        if (rightSum < curSum) {
            rightSum = curSum;
        }
    }

    return (leftSum + rightSum);
}

int maxSumSubarray(int a[], int low, int high) {
    if (low == high) {
        return (a[low]);
    } 
   
    int mid = (low + high) / 2;

    return max(maxSumSubarray(a, low, mid), maxSumSubarray(a, mid + 1, high), maxCrossingSum(a, low, mid, high));
}

int main() { // frp
    int n;
    scanf("%d", &n);

    int* a = new int [n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    int result = maxSumSubarray(a, 0, n - 1);
    printf("%d\n", result);
    
    return 0;
}

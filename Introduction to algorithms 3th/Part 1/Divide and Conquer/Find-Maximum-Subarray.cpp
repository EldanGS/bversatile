#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define frp freopen("input.txt", "r", stdin); \
            freopen("output.txt", "w", stdout); 

int leftIndex;
int rightIndex;

int Find_max_crossing_subarray(vector <int> a, int low = 0, int mid = 0, int high = 0) {
    int leftSum = 0;
    for (int i = mid; i >= 0; i--) {
        static int curSum = 0;
        curSum += a[i];

        if (leftSum < curSum) {
            leftSum = curSum;
            leftIndex = i;
        }
    }

    int rightSum = 0;
    for (int i = mid + 1; i <= high; i++) {
        static int curSum = 0;
        curSum += a[i];

        if (rightSum < curSum) {
            rightSum = curSum;
            rightIndex = i;
        }
    }

    return (leftSum + rightSum);
}

int Find_max_subarray(vector <int> a, int low, int high) {
    if (low == high) {
        return (a[low]);
    } else {
        int mid = (low + high) / 2;

        int leftSum = Find_max_crossing_subarray(a, low, mid);
        int rightSum = Find_max_crossing_subarray(a, mid + 1, high);
        int crossSum = Find_max_crossing_subarray(a, low, mid, high);

        if (leftSum >= rightSum and leftSum >= crossSum) {
            return leftSum;
        } else if (rightSum >= leftSum and rightSum >= crossSum) {
            return rightSum;
        } else {
            return crossSum;
        }
    }
}

int main() { //frp
    int n;
    cin >> n;

    vector <int> a(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }

    cout << Find_max_subarray(a, 1, n);
    
    return 0;
}

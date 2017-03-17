/**
 * http://www.geeksforgeeks.org/dynamic-programming-set-15-longest-bitonic-subsequence/
 *
 * Given an array arr[0 … n-1] containing n positive integers, a subsequence of arr[] is called Bitonic if it is first increasing, then decreasing.
 * Write a function that takes an array as argument and returns the length of the longest bitonic subsequence.
 * A sequence, sorted in increasing order is considered Bitonic with the decreasing part as empty. 
 * Similarly, decreasing order sequence is considered Bitonic with the increasing part as empty.
 */
 
 #include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define frp freopen("input.txt", "r", stdin); \
            freopen("output.txt", "w", stdout); 


int main() {  frp
    vector <int> array{1, 11, 2, 10, 4, 5, 2, 1};
    // Output: 6 (A Longest Bitonic Subsequence of length 6 is 1, 2, 10, 4, 2, 1)
    /* 
    lbs() returns the length of the Longest Bitonic Subsequence in
    arr[] of size n. The function mainly creates two temporary arrays
    lis[] and lds[] and returns the maximum lis[i] + lds[i] - 1.
 
    lis[i] ==> Longest Increasing subsequence ending with arr[i]
    lds[i] ==> Longest decreasing subsequence starting with arr[i]
    */

    int n = (int)array.size();
            
    vector <int> lis(n, 1);
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (array[i] > array[j] and lis[i] < lis[j] + 1) {
                lis[i] = lis[j] + 1;
            }
        }
    }

    vector <int> lds(n, 1);
    for (int i = n - 2; i >= 0; i--) {
        for (int j = n - 1; j > i; j--) {
            if (array[i] > array[j] and lds[i] < lds[j] + 1) {
                lds[i] = lds[j] + 1;
            }
        }
    }

    vector <int> lbs(n, 0);
    for (int i = 0; i < n; i++) {
        lbs[i] = lis[i] + lds[i] - 1;
    }

    cout << "Maximum Bitonice subsequence " << *max_element(lbs.begin(), lbs.end());

    return 0;
}
 
 

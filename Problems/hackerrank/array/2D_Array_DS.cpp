// https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


"""
Solution.
Complexity analysis:
Time: O(N^2) - always
Memory: O(1) - in worst case
"""

#include <bits/stdc++.h>

using namespace std;

// Complete the hourglassSum function below.
int hourglassSum(vector<vector<int>> arr) {
    int maxSum = -(int)2e9;

    for (int i = 0; i < 4; i++) {
        int currentSum = 0;
        for (int j = 0; j < 4; j++) {
            currentSum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] 
                        + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2];
            maxSum = max(maxSum, currentSum);
        }
    }

    return maxSum;
}

int main() {
    ofstream fout(getenv("OUTPUT_PATH"));

    vector<vector<int>> arr(6);
    for (int i = 0; i < 6; i++) {
        arr[i].resize(6);

        for (int j = 0; j < 6; j++) {
            cin >> arr[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int result = hourglassSum(arr);

    fout << result << "\n";

    fout.close();

    return 0;
}


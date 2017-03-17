/*
 * Coin changing problem:
 * 1) Given set of coins and a total, how many combinations to get total sum
 * 2) Given set of coins and a total, which of minimum changing to get total sum
 */ 
 
 // 1.
#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define frp freopen("input.txt", "r", stdin); \
            freopen("output.txt", "w", stdout); 

int main() {  frp
    int total = 5;
    vector <int> coins{1, 2, 3};
    int n = (int) coins.size();

    // O (n * m) space
    vector <vector <int> > combinations(n + 1, vector <int> (total + 1, 0));
    for (int i = 0; i < n; i++) {
        combinations[i][0] = 1;
    }

    for (int i = 1; i <= n; i++) {
        for (int num = 1; num <= total; num++) {
            if (coins[i - 1] > num) {
                combinations[i][num] = combinations[i - 1][num];
            } else {
                combinations[i][num] = combinations[i - 1][num] + combinations[i][num - coins[i - 1]];
            }
        }
    }

    cout << "Maximum count of combinations to get total sum is " << combinations[n][total] << "\n";


    // O(m) space
    vector <int> combinations(total + 1, 0);

    combinations[0] = 1;
    for (int i = 0; i < n; i++) {
        for (int num = 1; num <= total; num++) {
            if (num >= coins[i]) {
                combinations[num] += combinations[num - coins[i]];
            }
        }
    }

    cout << "Maximum count of combinations to get total sum is " << combinations[total] << "\n";



    return 0;
}

// 2.
#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define frp freopen("input.txt", "r", stdin); \
            freopen("output.txt", "w", stdout); 

const int INF = (int)1e9;

int main() {  frp
    int total = 11;
    vector <int> coins{1, 5, 6, 8};
    
    int n = (int)coins.size();
    vector <int> minChange(total + 1, INF);
    minChange[0] = 0;

    for (int i = 0; i < n; i++) {
        for (int num = 1; num <= total; num++) {
            if (coins[i] > num) {
                continue;
            }
            minChange[num] = min(minChange[num], minChange[num - coins[i]] + 1);
        }
    }

    if (minChange.back() >= INF) {
        cout << "We can't change!" << "\n";
    } else {
        cout << "Minimum element to change total sum is " << minChange[total] << "\n";
    }

    return 0;
}

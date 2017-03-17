/*
 * Find the longest increasing subsequence
 * O(n ^ 2) vs O(n * logn)
*/

#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define frp freopen("input.txt", "r", stdin); \
            freopen("output.txt", "w", stdout); 

int main() {  frp
    vector <int> array{1, 11, 2, 10, 4, 5, 2, 1};

    // O(n ^ 2);
    int n = (int)array.size();
    vector <int> lis(n, 1);
    vector <int> from(n, -1);

    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (array[i] > array[j] and lis[i] < lis[j] + 1) {
                lis[i] = lis[j] + 1;
                from[i] = j;
            }
        }
    }
    // 

    // Path
    int ans = lis[0], pos = 0;
    for (int i = 0; i < n; i++) {
        if (ans < lis[i]) {
            ans = lis[i];
            pos = i;
        }
    }

    cout << "Maximum length of increasing subsequence " << ans << "\n";
    
    vector <int> path;
    for (; pos != -1; pos = from[pos]) {
        path.push_back(pos);
    }

    cout << "Path: ";
    for (int i = (int)path.size() - 1; i >= 0; i--) {
        cout << path[i] << " \n"[i == 0];
    }
    //


    // O(n * logn);
    const int INF = (int)1e9;
    vector <int> lis(n, INF);
    lis[0] = -INF;

    int ans = 0;
    for (int i = 0; i < n; i++) {
        int pos = int(upper_bound(lis.begin(), lis.end(), array[i]) - lis.begin());

        if (lis[pos - 1] < array[i] and array[i] < lis[pos]) {
            lis[pos] = array[i];
            ans = max(ans, pos);
        }
    }   
    //

    cout << "Maximum length of increasing subsequence " << ans << "\n";

    return 0;
}

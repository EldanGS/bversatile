// "Brevity is the soul of wit."
#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define pb push_back
#define ull unsigned long long

typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;

int main() { boost
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif  
    int T;
    cin >> T;

    int n, k;
    for (int Case = 1; Case <= T; Case++) {
        cin >> n >> k;

        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        sort(a.begin(), a.end());

        int current = 0, counter = 0, answer = 0;
        for (int i = 0; i < n; i++) {
            if (a[i] > current) {
                counter++;
                answer++;
            } 
            if (counter == k) {
                current++;
                counter = 0;
            }
        }

        cout << "Case #" << Case << ": " << answer << "\n";
    }

    return 0;
}

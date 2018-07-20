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

const int mod = (int)1e9 + 7;

int n, cnt;
vector<vector<int> > g;

int dfs(int v, int parent) {
    int sum = 1;
    for (const int& to : g[v]) {
        if (to == parent) {
            continue;
        }
        sum += dfs(to, v);
    }

    if (sum % 2 == 0) {
        cnt++;
    }
    
    return sum;
}

int main() { boost
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
#endif  
    cin >> n;

    if (n & 1) {
        cout << "-1\n";
        return 0;
    }

    g.resize(n);
    for (int i = 1; i < n; i++) {
        static int u, v;
        cin >> u >> v;
        u--, v--;
        g[u].push_back(v);
        g[v].push_back(u);
    }

    dfs(0, -1);

    cout << cnt - 1 << "\n";

    return 0;
}

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

const int maxn = 100100;

int a[maxn], b[maxn];

double clac(int n, int cur, int cx, int cy, int cz, int x, int y, int z, int &xx, int &yy, int &zz) {
    if (cur == 3 * n) {
        int cc = 0;
        cc += xx > x;
        cc += yy > y;
        cc += zz > z;
        return cc > 1;
    }

    double ans = 0;
    if (cx < n) ans += clac(n, cur + 1, cx + 1, cy, cz, x + b[cur], y, z, xx, yy, zz);
    if (cy < n) ans += clac(n, cur + 1, cx, cy + 1, cz, x, y + b[cur], z, xx, yy, zz);
    if (cz < n) ans += clac(n, cur + 1, cx, cy, cz + 1, x, y, z + b[cur], xx, yy, zz);
    
    return ans;
}

int cnt;
double calc(int n, int cur, int cx, int cy, int cz, int x, int y, int z) {
    if (cur == 3 * n) {
        cnt++;
        return clac(n, 0, 0, 0, 0, 0, 0, 0, x, y, z);
    }

    double ans = 0;
    if (cx < n) ans = max(ans, calc(n, cur + 1, cx + 1, cy, cz, x + a[cur], y, z));
    if (cy < n) ans = max(ans, calc(n, cur + 1, cx, cy + 1, cz, x, y + a[cur], z));
    if (cz < n) ans = max(ans, calc(n, cur + 1, cx, cy, cz + 1, x, y, z + a[cur]));

    return ans;
}


int main() {
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int T; 
    scanf("%d", &T);

    for (int Case = 1; Case <= T; Case++) {
        cnt = 0;
        int n;
        scanf("%d", &n);
        for(int i = 0; i < 3 * n; i++) {
            scanf("%d", &a[i]);
        }
        for(int i = 0; i < 3 * n; i++) {
            scanf("%d", &b[i]);
        }

        printf("Case #%d: %.10lf\n", Case, calc(n, 0, 0, 0, 0, 0, 0, 0) / cnt);
    }

    return 0;
}

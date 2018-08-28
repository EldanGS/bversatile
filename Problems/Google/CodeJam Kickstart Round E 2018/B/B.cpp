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
const int maxn = 100100;

int ob[maxn];

bool cmp(pair<int, pair<int, int> > a, pair<int, pair<int, int> > b) {
    return make_pair(a.first, ob[a.second.first]) < make_pair(b.first, ob[b.second.first]);
}

char d[101][maxn];
bool b[101];   
int a[maxn];

int main() { boost
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif  
    int T;
    cin >> T;

    string s;
    int answer;
    int n, m, p;
    for (int Case = 1; Case <= T; Case++) {
        cin >> n >> m >> p;

        for (int i = 0; i < n; i++) {
            cin >> s;
            for(int j = 0; j < p; j++) {
                a[j] += s[j] == '1';
            }
        }
        for (int i = 0; i < m; i++) {
            cin >> d[i];
        }

        int answer = 0;
        vector<pair<int, pair<int, int> > > vc;
        for (int i = 0; i < p; i++) {
            if (a[i] > n - a[i]) {
                answer += a[i];
                vc.push_back(make_pair(a[i] + a[i] - n, make_pair(i, 1)));
                for(int j = 0; j < m; j++) {
                    ob[i] += d[j][i] == '0';
                }
            } else {
                answer += n - a[i];
                vc.push_back(make_pair(n - a[i] - a[i], make_pair(i, 0)));
                for(int j = 0; j < m; j++) {
                    ob[i] += d[j][i] == '1';
                }
            }
        }

        sort(vc.begin(), vc.end(), cmp);
        
        for (int i = 10; i < vc.size(); i++) {
            for(int j = 0; j < m; j++) {
                if(d[j][vc[i].second.first] - '0' != vc[i].second.second) {
                    b[j] = 1;
                }
            }
        }

        int choose = mod;
        vc.resize(min((int)vc.size(), 10));
        int sz = (int)vc.size();
        for (int i = 0; i < (1 << sz); i++) {
            bool ok = 1;
            for (int j = 0; j < m; j++) {
                if (b[j]) {
                    continue;
                }

                bool notOk = 0;
                for (int k = 0; k < sz; k++) {
                    bool cur = vc[k].second.second;
                    int pos = vc[k].second.first;
                    if (((i >> k) & 1)) {
                        cur ^= 1;
                    }
                    if (d[j][pos] - '0' != cur) {
                        notOk = 1;
                    }
                }

                ok &= notOk;
            }
            if (ok) {
                int notchoose = 0;
                for (int k = 0; k < sz; k++) {
                    if (((i >> k) & 1)) {
                        notchoose += vc[k].first;
                    }
                }
                choose = min(choose, notchoose);
            }
        }

        cout << "Case #" << Case << ": " << n * p - (answer - choose) << "\n";
        memset(a, 0, sizeof a);
        memset(b, 0, sizeof b);
        memset(ob, 0, sizeof ob);
    }

    return 0;
}

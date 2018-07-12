#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define pb push_back
#define eb emplace_back
#define mp make_pair
#define sqr(x) ((x * x))
#define sz(x) (int)x.size()
#define all(x) x.begin(), x.end()
#define frp freopen("input.txt", "r", stdin); \
		    freopen("output.txt", "w", stdout); 

typedef long long ll;
typedef vector <int> vi;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

const int maxn = (int)1e5 + 100;
const int inf = (int)1e9 * 2;
const int mod = (int)1e9 + 7;

int n, m;
ll fv[maxn];

inline ll query(ll r){
	ll res = 0;
	for(int i = r; i >= 0; i &= i + 1, i--){
		res += fv[i];
	}
	return res;
}

inline ll get_sum(int l, int r){
	return (query(r) - (l ? query(l - 1) : 0));
}

void update(int pos, int val){
	//val -= query(pos) - query(pos - 1);

	for(int i = pos; i < maxn; i |= i + 1){
		fv[i] += val;
	}
}

int main(){
	scanf("%d %d", &n, &m);
	int l, r, pos, val;
	while(m--){
		string s; cin >> s;
		if(s == "add"){
			scanf("%d %d", &pos, &val);
			update(pos, val);
			continue;
		}
		scanf("%d %d", &l, &r);
		printf("%lld\n", get_sum(l, r));
	}
	
	return 0;
}
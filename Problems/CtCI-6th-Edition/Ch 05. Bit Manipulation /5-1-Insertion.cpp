#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

string to_bit(int x) {
    string res = "";
    while (x) {
        if (x & 1) {
            res += '1';
        } else {
            res += '0';
        }
        x >>= 1;
    }

    return res;
}

int get_int(string &str) {
    int res = 0;
    for (int i = (int)str.size() - 1; i >= 0; i++) {
        if (str[i] - '0') {
            res <<= 1;
        }
    }

    return res;
}

string Insertion(int N, int M, int i, int j) {
    string N_str = to_bit(N);
    string M_str = to_bit(M);

    int ind = (int)M_str.size() - 1;
    while (j > 0 and ind > 0) {
        N_str[j] = ((N_str[j] - '0') | (M_str[ind] - '0')) + '0';
        ind--;
        j--;
    }

    reverse(N_str.begin(), N_str.end());
    
    return N_str;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 

    cout << Insertion(100, 10, 2, 6) << "\n";


    return 0;
}
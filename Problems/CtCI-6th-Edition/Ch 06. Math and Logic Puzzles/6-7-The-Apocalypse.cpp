#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

vector<int> getChild();
double runNFamilies(int n) {
    int boys = 0, girls = 0;
    for (int i = 0; i < n; i++) {
        auto genetic = getChild(); // get binary value, 1 if girl, otherwise boy
        girls += genetic[0];
        boys += genetic[1];
    }

    return girls / (girls + boys + 0.);
}

vector<int> getChild() {
    int random = rand() % 2;
    int boys = 0, girls = 0;
    while (girls == 0) {
        if (random) {
            girls++;
        } else {
            boys++;
        }
        random = rand() % 2;
    }

    return {girls, boys};
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 

    cout << runNFamilies(10) << "\n";


    return 0;
}
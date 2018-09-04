#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

void setZeroes(vector<vector<int> >& matrix) {
    int n = (int)matrix.size();
    int m = (int)matrix[0].size();
    int row = 1, col = 1;
    for (int i = 0; i < n; i++) {
        if (!matrix[i][0]) {
            row = 0;
            break;
        }
    }
    for (int j = 0; j < m; j++) {
        if (!matrix[0][j]) {
            col = 0;
            break;
        }
    }
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            if (!matrix[i][j]) {
                matrix[i][0] = matrix[0][j] = 0;
            }
        }
    }
    for (int i = 1; i < n; i++) {
        if (!matrix[i][0]) {
            for (int j = 0; j < m; j++) {
                matrix[i][j] = 0;
            }
        }
    }
    for (int j = 1; j < m; j++) {
        if (!matrix[0][j]) {
            for (int i = 0; i < n; i++) {
                matrix[i][j] = 0;
            }
        }
    }
    if (!row) {
        for (int i = 0; i < n; i++) {
            matrix[i][0] = 0;
        }
    }
    if (!col) {
        for (int j = 0; j < m; j++) {
            matrix[0][j] = 0;
        }
    }
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    int n, m;
    cin >> n >> m;

    vector<vector<int> > matrix(n, vector<int> (m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> matrix[i][j];
        }
    }

    cout << "Actual matrix\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << matrix[i][j] << " \n"[j == m - 1];
        }
    }
    
    setZeroes(matrix);

    cout << "Transform matrix\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << matrix[i][j] << " \n"[j == m - 1];
        }
    }

    return 0;
}
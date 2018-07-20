// "Brevity is the soul of wit."
#include <stdio.h>
#include <bits/stdc++.h>
  
using namespace std;
 
typedef long long ll;
 
#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
 
int n;
char a[44][44];
const int dx[] = {1, -1, 0, 0}; 
const int dy[] = {0, 0, 1, -1};
 
bool canMove(int x, int y) {
    return (1 <= x and x <= n) and (1 <= y and y <= n);
}
 
int main() { boost
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif  
    cin >> n;
 
    int startI, startJ;
    int finishI, finishJ;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> a[i][j];
 
            if (a[i][j] == 'X') {
                startI = i;
                startJ = j;
            }
            if (a[i][j] == '@') {
                finishI = i;
                finishJ = j;
            }
        }
    }
 
    queue <pair<int, int> > q;
    q.push(make_pair(startI, startJ)); // startI = x, startJ = y;
 
    vector<vector<int> > distance(n + 1, vector<int>(n + 1, -1));
    distance[startI][startJ] = 0;
 
    while (!q.empty()) {
        auto v = q.front();
        q.pop();
 
        for (int i = 0; i < 4; i++) {
            int x = v.first;
            int y = v.second;
 
            int nextX = dx[i] + x;
            int nextY = dy[i] + y;
 
            if (canMove(nextX, nextY) and (a[nextX][nextY] == '.' or a[nextX][nextY] == '@') and distance[nextX][nextY] == -1) {
                distance[nextX][nextY] = distance[x][y] + 1;
                q.push(make_pair(nextX, nextY));
            } 
        }
    }
    
    // path recovery
    if (distance[finishI][finishJ] == -1) {
        cout << "No\n";
        return 0;
    }
 
    while (distance[finishI][finishJ] != 0) {
        for (int i = 0; i < 4; i++) {
            int prevX = dx[i] + finishI; // prev = previous
            int prevY = dy[i] + finishJ;
 
            if (canMove(prevX, prevY) and distance[finishI][finishJ] == distance[prevX][prevY] + 1) {
                a[prevX][prevY] = '+';
                finishI = prevX;
                finishJ = prevY;
            }
        }
    }
    a[startI][startJ] = '+';
 
    cout << "Yes\n";
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << a[i][j];
        }
        cout << "\n";
    }
 
 
    return 0;
}
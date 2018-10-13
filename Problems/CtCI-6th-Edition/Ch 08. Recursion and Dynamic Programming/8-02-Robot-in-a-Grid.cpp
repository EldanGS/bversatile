#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

struct Point {
    int row;
    int column;

    Point(int r, int c) :
        row(r),
        column(c)
    {}
};

bool getPath(vector<vector<int> > maze, int r, int c, vector<Point*>& path, unordered_set<Point*>& data) {
    if (r < 0 or c < 0 or maze[r][c] == -1) {
        return false;
    }

    Point* currPos = new Point(r, c);

    if (data.find(currPos) != data.end()) {
        return false;
    }

    bool atOrigin = (r == 0) and (c == 0);
    if (atOrigin or getPath(maze, r - 1, c, path, data) \
                or getPath(maze, r, c - 1, path, data)) {
        path.push_back(currPos);
        return true;
    }

    data.insert(currPos);

    return false;
}   

vector<Point*> getPath(vector<vector<int> > maze) {
    unordered_set<Point*> data;
    vector<Point*> path;
    getPath(maze, maze.size() - 1, maze[0].size() - 1, path, data);

    return path;
}


int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    int rows = 5, cols = 7;
    vector<vector<int> > maze(rows, vector<int>(cols, 0));

    maze[1][3] = -1;
    maze[2][5] = -1;
    maze[3][2] = -1;
    maze[0][1] = -1;

    vector<Point*> path = getPath(maze);
    if (path.empty()) {
        cerr << "Path does not exist!" << endl;
    } else {
        for (int i = 0; i < (int)path.size(); i++) {
            cout << "[" << path[i]->row << "]" << "[" << path[i]->column << "]" << endl;
        }   
    }

    return 0;
}
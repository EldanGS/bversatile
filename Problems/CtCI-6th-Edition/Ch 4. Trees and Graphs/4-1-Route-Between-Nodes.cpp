#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

class Graph {
public:
    int v; // number of vertices
    std::vector<int> *adj; // adjacency list

    Graph(int v);
    void addEdge(int from, int to);
    bool isRoute(int from, int to);
};

// Constructor
Graph::Graph(int v) {
    this -> v = v;
    this -> adj = new std::vector<int>[v];
}

// add Edge from -> to
void Graph::addEdge(int from, int to) {
    adj[from].push_back(to);
}

bool Graph::isRoute(int from, int to) {
    vector<bool> visited(v, false);
    queue<int> q;

    q.push(from);
    while (!q.empty()) {
        int v = q.front();
        q.pop();

        if (v == to) {
            return true;
        }
        visited[v] = true;

        for (int u : adj[v]) {
            if (!visited[u]) {
                q.push(u);
            }
        }
    }

    return false;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    Graph g(6);
    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);

    int x = 5, y = 4;
    if (g.isRoute(x, y)) {
        cout << "from " << x << " to " << y << " has route\n";
    } else {
        cout << "from " << x << " to " << y << " has not route\n";
    }

    x = 5, y = 1;
    if (g.isRoute(x, y)) {
        cout << "from " << x << " to " << y << " has route\n";
    } else {
        cout << "from " << x << " to " << y << " has not route\n";
    }

    return 0;
}
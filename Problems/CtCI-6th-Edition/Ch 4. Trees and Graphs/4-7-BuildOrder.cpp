#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

class Node {
    vector<char> *graph;
    vector<char> projects;
    vector<bool> visited;
    vector<char> answer;
    vector<pair<char, char> > dependencies;
public:
    Node(vector<char> projects, vector<pair<char, char> > dependencies);

    void addDependencies(vector<pair<char, char> > dependencies);

    void dfs(char v) {
        visited[v] = true;
        for (char to : graph[v]) {
            if (!visited[to]) {
                dfs(to);
            }
        }

        answer.push_back(v);
    }

    void buildOrder() {
        visited.assign(256, false);
        answer.clear();

        for (char v : projects) {
            if (!visited[v]) {
                dfs(v);
            }
        }

        reverse(answer.begin(), answer.end());
    }

    void printOrder() {
        for (int i = 0; i < (int)answer.size(); i++) {
            cout << answer[i];
            if (i + 1 < (int)answer.size()) {
                cout << ", ";
            }
        }
        cout << "\n";
    }
};

Node::Node(vector<char> projects, vector<pair<char, char> > dependencies) {
    this -> graph = new vector<char>[256];
    this -> projects = projects;
    this -> dependencies = dependencies;
}

void Node::addDependencies(vector<pair<char, char> > dependencies) {
    for (pair<char, char> it : dependencies) {
        graph[it.first].push_back(it.second);
    }
}


int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    vector<char> projects{'a', 'b', 'c', 'd', 'e', 'f'};
    vector<pair<char, char> > dependencies{{'a', 'b'}, {'f', 'b'}, {'b', 'd'}, {'f', 'a'}, {'b', 'c'}};

    Node sequence = Node(projects, dependencies);

    sequence.addDependencies(dependencies);
    sequence.buildOrder();
    sequence.printOrder();

    return 0;
}
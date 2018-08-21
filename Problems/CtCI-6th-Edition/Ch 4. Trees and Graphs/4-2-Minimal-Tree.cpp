#include <bits/stdc++.h>

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

struct Node {
    int val;
    Node * left;
    Node * right;

    Node(int x) :
        val(x),
        left(NULL),
        right(NULL)
    {}
};

void preorder(Node * node) {
    if (!node) {
        return;
    }
    cout << node -> val << " ";
    preorder(node -> left);
    preorder(node -> right);
}

Node * createMinimalBST(vector<int> nums, int left, int right) {
    if (left > right) {
        return NULL;
    }

    int mid = (left + right) / 2;
    Node * node = new Node(nums[mid]);
    node -> left = createMinimalBST(nums, left, mid - 1);
    node -> right = createMinimalBST(nums, mid + 1, right);

    return node;
}

Node * createMinimalBST(vector<int> nums) {
    int n = (int)nums.size();

    return createMinimalBST(nums, 0, n - 1);
}


int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 

    vector<int> a;
    for (int i = 1; i <= 7; i++) {
        a.push_back(i);
    }

    cout << "Sorted array:\n";
    for (int val : a) {
        cout << val << " ";
    }

    cout << "\nminimal BST:\n";

    Node * root = createMinimalBST(a);
    preorder(root);

    /*
        Convert List to BST {1,2,3,4,5,6,7}
                         4
                      /     \
                    2         6
                  /   \     /   \
                 1     3   5     7
    */

    return 0;
}
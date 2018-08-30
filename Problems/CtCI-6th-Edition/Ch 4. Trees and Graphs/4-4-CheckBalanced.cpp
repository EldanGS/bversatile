#include "TreeNodeConstructor.h"
#include "ListConstructor.h"

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

int getHeight(TreeNode *node);

bool isTreeBalanced(TreeNode *root) {
    return getHeight(root) != -1;
}

int getHeight(TreeNode *node) {
    if (!node) {
        return 0;
    }

    int left = getHeight(node -> left);
    if (left == -1) {
        return -1;
    }

    int right = getHeight(node -> right);
    if (right == -1) {
        return -1;
    }

    if (abs(left - right) > 1) {
        return -1;
    }

    return max(left, right) + 1;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 

    /* Constructed binary tree is
                Unbalanced
                    1
                   / \
                  2   3
                 /   /
                4    6
               / 
              5

                Balanced
                    1
                   / \
                  2   3
                 /   /
                4    6
    */

    TreeNode *root = new TreeNode(1);
    root -> left = newnode(2);
    root -> right = newnode(3);
    root -> left -> left = newnode(4);
    root -> right -> left = newnode(6);
    // root -> left -> left -> left = newnode(5); // Depends of this node, we will constructed balanced tree or not;

    if (isTreeBalanced(root)) { 
        cout << "Balanced\n";
    } else {
        cout << "Unbalanced\n";
    }

    return 0;
}
#include "TreeNodeConstructor.h"

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

bool checkBST(TreeNode *root, int minValue, int maxValue);

bool isValidBST(TreeNode *root) {
    return checkBST(root, INT_MIN, INT_MAX);
}

bool checkBST(TreeNode *root, int minValue, int maxValue) {
    if (!root) {
        return true;
    }

    if (root -> value <= minValue or root -> value >= maxValue) {
        return false;
    }

    return checkBST(root -> left, minValue, root -> value)
        and checkBST(root -> right, root -> value, maxValue);
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 

    /* Constructed binary tree is
                 
                  5
                /  \
              3    7
             / \  / \
            2  4 6  8
           /
          1
    */

    TreeNode *root = new TreeNode(5);
    root -> left = newnode(3);
    root -> right = newnode(7);
    
    root -> left -> left = newnode(2);
    root -> left -> right = newnode(4);
    root -> right -> left = newnode(6);
    root -> right -> right = newnode(8);

    root -> left -> left -> left = newnode(1);
    
    if (isValidBST(root)) {
        cout << "Valid BST\n";
    } else {
        cout << "Not valid BST\n";
    }

    return 0;
}

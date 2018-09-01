#include "TreeNodeConstructor.h"

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

// Solutions                  Runtime                   Preference
// ---------------------------------------------------------------
// 0) If BST, trace Paths     O(log n) if balanced      Clever
// 1) Use links to parents    O(log n) if balanced      Clever
// 2) Recursive               O(n)                      Favorite

TreeNode *commonAncestor(TreeNode *root, TreeNode *p, TreeNode *q) {
    if (!root or root == p or root == q) {
        return root;
    }
    
    TreeNode *left = commonAncestor(root -> left, p, q);
    TreeNode *right = commonAncestor(root -> right, p, q);

    if (!left) {
        return right;
    } else if (!right) {
        return left;
    } else {
        return root;
    }
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 
    /* Constructed binary tree is
                1
               / \
              4    9
             /\   / \
            5 6 11  10
             /   \
            15    8        
    */

    TreeNode *root = new TreeNode(1);
    root -> left = newnode(4);
    root -> right = newnode(9);

    root -> left -> left = newnode(5);
    root -> left -> right = newnode(6); 
    root -> right -> left = newnode(11);
    root -> right -> right = newnode(10);

    root -> left -> right -> left = newnode(15);

    auto result = commonAncestor(root, root -> left -> right -> left, root -> left -> left); // between 15, 5
    if (result) {
        cout << "Common ancestor = " << result -> value << "\n";
    } else {
        cout << "No common ancestor\n";
    }

    return 0;
}
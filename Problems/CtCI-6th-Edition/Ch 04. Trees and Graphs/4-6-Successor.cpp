#include "TreeNodeConstructor.h"

using namespace std;

#define boost ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

/*
Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. 
You may assume that each node has a link to its parent.
*/

TreeNode *leftMostChild(TreeNode *node);
TreeNode *properParent(TreeNode *node);

TreeNode *InorderSuccessor(TreeNode *node) {
    // if node has right side, which is mean we will elements more current node. 
    // Otherwise, we will try to claimb to ancestor.
    if (node -> right) {
        return leftMostChild(node -> right);
    } else {
        return properParent(node);
    }
}

TreeNode *leftMostChild(TreeNode *node) {
    if (!node) {
        return NULL;
    }

    // Fall to left most child of current node
    TreeNode *child = node;
    while (child -> left) {
        child = child -> left;
    }

    return child;
}

TreeNode *properParent(TreeNode *node) {
    if (!node) {
        return NULL;
    }

    // Get parent of current node, and try to climb-up to ancestor
    TreeNode *parent = node -> parent;
    TreeNode *child = node;
    while (parent and parent -> left != child) {
        child = parent;
        parent = child -> parent;
    }

    return parent;
}

int main() { boost;
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
#endif 

    /* Constructed binary tree is
            1
             \
              7
             /
            5
           /
          2
    */

    TreeNode * root = new TreeNode(1);
    root -> right = newnode(7);
    root -> right -> parent = root;
    
    root -> right -> left = newnode(5);
    root -> right -> left -> parent = root -> right;
    
    root -> right -> left -> left = newnode(2);
    root -> right -> left -> left -> parent = root -> right -> left;

    auto answer = InorderSuccessor(root);
    if (answer) {
        cout << answer -> value << "\n"; 
    } else {
        cout << "No answer\n";
    }

    return 0;
}